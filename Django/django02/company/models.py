#!/usr/bin/evn python
#coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserType(models.Model):
    name=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
class UserInfo(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()
    user_type=models.ForeignKey('UserType')

    def __unicode__(self):
        temp = "%s %s %s %s %s" %(self.username,self.password,self.email,self.user_type_id,self.user_type.name)
        return temp

class UserGroup(models.Model):
    groupname=models.CharField(max_length=50)
    user=models.ManyToManyField('UserInfo')

    def __unicode__(self):
        temp = "%s %s %s " %(self.groupname,self.user_id,self.user.username)
        return temp
    
class Assert(models.Model):
    hostname=models.CharField(max_length=256)
    ip=models.GenericIPAddressField()
    user_group=models.ForeignKey('UserGroup')
    
    def __unicode__(self):
        temp = "%s %s %s %s" %(self.hostname,self.ip,self.user_group_id,self.user_group.groupname)
        return temp