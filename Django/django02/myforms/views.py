#!/usr/bin/evn python
#coding=utf-8

from django.shortcuts import render, render_to_response
from myforms import forms
from django.http.response import HttpResponse
import json

# Create your views here.

def login(request):
    ret={'data':'','error':''}
    obj=forms.ALogin()
    ret['data']=obj
    errorObj=''
    if request.method=='POST':
        checkForm=forms.ALogin(request.POST)
        checkResult=checkForm.is_valid()
        if checkResult:
            pass
        else:
#             errorObj= checkForm.errors
            errorObj= checkForm.errors.as_data().values()[0][0].messages[0]
            ret['error']=errorObj 
            ret['data']=checkForm
    return render_to_response('myforms/login.html',ret)

def ajax(request):
    print "ajax"
    if request.method=='POST':
#         user=request.POST.get('dat',None)
#         print user
        data={'status':0,'msg':'request success','data':[11,22,33]}
        return HttpResponse(json.dumps(data))
    return render_to_response('myforms/ajax.html')




