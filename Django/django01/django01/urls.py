#!/usr/bin/evn python
#coding=utf-8

"""django01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from app01.views import *

urlpatterns = [
    ###################################################
    #测试路由方法 

#     url(r'^index/', index),
#     url(r'^login/', login),
#     #一个数字参数    http://127.0.0.1:9000/list/20
#     url(r'^list/(\d*)', list),
#     #两个数字参数    http://127.0.0.1:9000/list2/20/40
#     url(r'^list2/(\d*)/(\d*)', list2),
#     #模板                http://127.0.0.1:9000/list3/20
#     url(r'^list3/(?P<name>\d*)', list3),
#     #模板 多参数    http://127.0.0.1:9000/list4/20/800/
#     url(r'^list4/(?P<name>\d*)/(?P<id>\d*)/', list4),
#     #默认参数        http://127.0.0.1:9000/list5/90/ 后面的是默认参数
#     url(r'^list5/(?P<name>\d*)/(?P<id>\d*)/$', list5), #注意最后的/ 必须加,但是默认值的时候回有问题 加$ 这没有这个问题
#     url(r'^list5/(?P<name>\d*)/$', list5,{'id':200}),
    
#     url(r'^admin/', admin.site.urls),
    #如果一个项目里边有多个app,url怎么写
     url(r'^app01/', include('app01.urls')),
     
     url(r'^app02_db/', include('app02_db.urls')),
    
]
