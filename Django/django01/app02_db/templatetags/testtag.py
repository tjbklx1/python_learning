#!/usr/bin/env python
#coding:utf-8
from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError
 
register = template.Library()
 
@register.simple_tag
def mymethod(v1):
    return  v1 * 1000 