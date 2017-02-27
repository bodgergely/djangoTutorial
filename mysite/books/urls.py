'''
Created on Feb 27, 2017

@author: Gergely
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]