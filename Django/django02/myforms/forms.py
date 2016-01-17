#!/usr/bin/evn python
#coding=utf-8

from django import forms 

class ALogin(forms.Form):
    username=forms.CharField(required=True,
        error_messages={'required':('username is required !!!'),'invalid':('username format error')})
    email=forms.EmailField(required=True,
        error_messages={'required':('email is required !!!'),'invalid':('email format error')})
    ip=forms.CharField()