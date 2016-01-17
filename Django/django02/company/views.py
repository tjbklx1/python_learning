#!/usr/bin/evn python
#coding=utf-8

from django.shortcuts import render, render_to_response, redirect
from company.models import *
from django.http.response import HttpResponse

# Create your views here.
def register(request):
    '''
    #创建用户类型
    t1=UserType.objects.create(name='系统管理员')
    t2=UserType.objects.create(name='普通管理员')
    #创建用户
    u1=UserInfo.objects.create(username='admin',
                                      password='admin',
                                      email='admin@admin.com',
                                      user_type=t1)
    #第二种方式创建用户
    t3=UserType.objects.get(name='普通管理员')
    u2=UserInfo.objects.create(username='abc',
                                      password='abc',
                                      email='abc@abc.com',
                                      user_type=t3)
    
    #创建用户组
    group1=UserGroup.objects.create(groupname='系统管理组')
    group1.user.add(u1)
    group2=UserGroup.objects.create(groupname='数据库管理组')
    
    '''
    return HttpResponse('<h1>注册成功</h1>')
    
def login(request):
    print 'login'
    ret={'status':''}
    
    if request.method=='POST':
        user=request.POST.get('username',None)
        pwd=request.POST.get('password',None)
        print user,pwd
        is_empty=all([user,pwd])
        if is_empty:
            count =UserInfo.objects.filter(username=user,password=pwd).count()
            if count == 1:
                return redirect('/company/index')
            else:
                ret['status']='username or password error'
        else:
            ret['status']='username or password cannot empty'

    
    return render_to_response('company/login.html',ret)
     
def index(request):
    print 'index'
    return render_to_response('company/index.html')


def host(request):
    print 'host'
    # data 用做host列表的展示,group作为group下拉选项的展示
    ret={'status':'','data':None,'group':None}
    usergroup =UserGroup.objects.all()
    ret['group']=usergroup
    
    #添加主机请求
    if request.method=='POST':
        hostname=request.POST.get('hostname',None)
        ip=request.POST.get('ip',None)
        groupID=request.POST.get('group',None)
        print hostname,ip,groupID
        is_empty=all([hostname,ip,groupID])
        
        if is_empty:
            groupObj=UserGroup.objects.get(groupname=groupID)
            Assert.objects.create(hostname=hostname,ip=ip,user_group=groupObj)
        else:
            ret['status']='hostname or ip cannot be null'
    
    data=Assert.objects.all()
    ret['data']=data

    return render_to_response('company/host.html',ret)
    
    
def user(request):
    print 'user'
    return render_to_response('company/user.html')


def group(request):
    print 'group'
    return render_to_response('company/group.html')


def testcase(request):
#     alluser=UserInfo.objects.all()
#     alluser=UserInfo.objects.get(id=3)
#     alluser=UserInfo.objects.filter(id>2)    #error
#     alluser=UserInfo.objects.filter(id__gt=2)
#     alluser=UserInfo.objects.filter(user_type_id__gt=3)
#     alluser=UserInfo.objects.filter(user_type__name=u'系统管理员')
    alluser=UserInfo.objects.filter(user_type__name__contains=u'管理员')
    
    
    print alluser
    return HttpResponse(alluser)