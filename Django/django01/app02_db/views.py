#!/usr/bin/evn python
#coding=utf-8

from django.shortcuts import render, render_to_response
from app02_db.models import *
from app02_db.forms import *
from django.http.response import HttpResponse
# Create your views here.

def add(request,name):
    Assert.objects.create(hostname=name)
    return HttpResponse('ok')

def save(request,name):
    obj=Assert(hostname=name)
    obj.save()
    return HttpResponse('ok')
    
def delete(request,id):
    Assert.objects.get(id=id).delete()
    return HttpResponse('ok')

def update(request,id,name):
    print id,name
    obj=Assert.objects.get(id=id)
    obj.hostname=name 
    obj.save()
    return HttpResponse('ok')

def update2(request,id,name):
    #id__gt  注意是双下划线
    Assert.objects.filter(id__gt=id).update(hostname=name)
    return HttpResponse('ok')

def get(request,name):
    assetList= Assert.objects.filter(hostname__contains=name)
    print assetList
    for item in assetList:
        print item.id,item.hostname
    return HttpResponse('ok')


def getAll(request):
    print "=======get all=================="
    assetList= Assert.objects.all()
    print assetList.query
    for item in assetList:
        print item.id,item.hostname
        
    print "=======get page=================="    
    pageList= Assert.objects.all()[0:2]
    print pageList.query
    for item in pageList:
        print item.id,item.hostname
        
    print "=======get order desc=================="
    orderList=Assert.objects.all().order_by("-id")
    print orderList.query
    for item in orderList:
        print item.id,item.hostname
        
    print "=======get order asc=================="
    orderList=Assert.objects.all().order_by("id")
    print orderList.query
    print orderList
    for item in orderList:
        print item.id,item.hostname
        
    print "=======get all columns================"
    assetList2= Assert.objects.all().values('id','hostname')
    print assetList2.query
    print assetList2
    for item in assetList2:
        print item['id'],item['hostname']
        
    return HttpResponse('ok')


def AssertList(request):
    assetList= Assert.objects.all()
    return render_to_response('assertlist.html',{'data':assetList,'user':'running man'})

def AssertList2(request):
    # test tag
    assetList= Assert.objects.all()
    return render_to_response('assertlist2.html',{'data':assetList,'user':'running man'})

def AssertList3(request):
    #test 母版 子版
    assetList= Assert.objects.all()
    return render_to_response('assertlist3.html',{'data':assetList,'user':'running man'})

def login(request):
    # test 表单
    #登录页 不和头部底部共用
    if request.method=='POST':
        user=request.POST.get('username',None)
        pwd=request.POST.get('password',None)
        print user,pwd
        '''
        try:
            UserInfo.objects.get(username=user,password=pwd)
        except Exception,e:
            pass 
        '''
        result = UserInfo.objects.filter(username=user,password=pwd).count()
        if result ==1:
            return render_to_response('login success')
        else:
            return render_to_response('login.html',{'status':'username or password error'})
    else:
        return render_to_response('login.html')


def register(request):
    registerform=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print data
        else:
            temp=form.errors.as_data()
            print temp
            print type(temp)
            print temp['email']
            print type(temp['email'])
            print temp['email'][0]
            
        return render_to_response('register.html',{'form':registerform})
    else:   
        return render_to_response('register.html',{'form':registerform})
