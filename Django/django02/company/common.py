#!/usr/bin/evn python
#coding=utf-8

def try_int(arg,default):
    try:
        arg=int(arg)
    except Exception , e:
        arg=default
    return arg
        