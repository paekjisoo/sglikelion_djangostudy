from django.shortcuts import get_object_or_404, redirect, render
from .models import Homework
from django.utils import timezone
from .forms import HomeworkForm

# Create your views here.
def homework_index(request):
    return render(request, 'homepage/homework_index.html', {})

def homework_list(request):
    homeworks = Homework.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'homepage/homework_list.html', {'homeworks': homeworks})

def homework_detail(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    return render(request, 'homepage/homework_detail.html', {'homework':homework})

def homework_new(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST, request.FILES)
        if form.is_valid():
            homework = form.save(commit=False)
            homework.author = request.user
            homework.published_date = timezone.now()
            homework.save()
            return redirect('homework_detail', pk=homework.pk)
    else:
        form = HomeworkForm()
    return render(request, 'homepage/homework_edit.html', {'form': form})

def homework_edit(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    if request.method == "POST":
        form = HomeworkForm(request.POST, request.FILES, instance=homework)
        if form.is_valid():
            homework = form.save(commit=False)
            homework.author = request.user
            homework.published_date = timezone.now()
            homework.save()
            return redirect('homework_detail', pk=homework.pk)
    else:
        form = HomeworkForm(instance=homework)
    return render(request, 'homepage/homework_edit.html', {'form': form})