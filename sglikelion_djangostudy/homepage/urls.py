from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homework_index, name='homework_index'),
    url(r'^homepage/homework/list/$', views.homework_list, name='homework_list'),
    url(r'^homepage/homework/(?P<pk>\d+)/$', views.homework_detail, name='homework_detail'),
    url(r'^homepage/homework/new/$', views.homework_new, name='homework_new'),
    url(r'^homepage/homework/edit/(?P<pk>\d+)/$', views.homework_edit, name='homework_edit'),
]

