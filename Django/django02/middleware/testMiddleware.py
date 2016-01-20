#!/usr/bin/evn python
#coding=utf-8

from django.http.response import HttpResponse

class testMiddleware(object):
    
    def process_request(self,request):
        print "1.process_request"
#         print "404"
#         return HttpResponse("404")
        
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print "2.process_view"
        
    def process_exception(self, request, exception):
        print "3.process_exception"
     
    def process_response(self, request, response):
        print "4.process_response"
        return response    

