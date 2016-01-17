#!/usr/bin/evn python
#coding=utf-8

from django.conf.urls import url,include
from django.contrib import admin

from views import *
urlpatterns = [

    url(r'^add/(?P<name>\d*)/$',add),
    url(r'^save/(?P<name>\d*)/$',save),
    url(r'^delete/(?P<id>\d*)/$',delete),
    url(r'^update/(?P<id>\d*)/(?P<name>\d*)/$',update),
    url(r'^update2/(?P<id>\d*)/(?P<name>\w*)/$',update2),           
    url(r'^get/(?P<name>\d*)/$',get),
    url(r'^getAll/$',getAll),
    url(r'^AssertList/$',AssertList),
    url(r'^AssertList2/$',AssertList2),
    url(r'^AssertList3/$',AssertList3),
    url(r'^login/$',login),
    url(r'^register/$',register),
]