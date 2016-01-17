from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    print "index"
    return HttpResponse('index')
    
def login(request):
    print "login"
    return HttpResponse('login')
    
def list(request,id):
    print "list id : %s " %id
    return HttpResponse('list')

def list2(request,id1,id2):
    print "list2 id : %s ,%s" % (id1,id2)
    return HttpResponse('list2')

def list3(request,name):
    print "list3 name : %s " %name
    return HttpResponse('list3')    

def list4(request,id,name):
    print "list4 id, name : %s ,%s" %(id,name)
    return HttpResponse('list4')    

def list5(request,id,name):
    print "list5 id, name : %s ,%s" %(id,name)
    return HttpResponse('list5')   
