'''
Created on Feb 27, 2017

@author: Gergely
'''

from django.conf.urls import url

from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/books/2
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]