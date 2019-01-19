from django.shortcuts import render
import re

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split(' ')
    word_dic = {}

    for word in words:

        word = word[:-1] + re.sub('[,.!?~]', '', word[-1])
                
        if word in word_dic:
            # increase
            word_dic[word]+=1
        else:
            if word.endswith("은") or word.endswith("는") or word.endswith("이") or word.endswith("가"):
                word = word[:-1]

            # add to dic
            word_dic[word]=1

    return render(request, 'wordcount/result.html', {"full": text, "total": len(words), "sorted_dic": sorted(word_dic.items(), key=lambda x: x[1], reverse=True)})
