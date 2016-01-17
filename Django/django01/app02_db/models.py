#!/usr/bin/evn python
#coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserType(models.Model):
    name=models.CharField(max_length=50)
    
class UserInfo(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.BooleanField(default=False)
    age=models.IntegerField(default=20)
    memo=models.TextField(default='')
    createdate=models.DateTimeField(default='2016-01-01 00:01')

    #外键 建立一个外键 app02_db_userinfo_typeid_id_ea466575_fk_app02_db_usertype_id
    typeid=models.ForeignKey(UserType)
    
class Group(models.Model):
    name=models.CharField(max_length=50)
    
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    #多对多 简历一个多多对app02_db_user_group_relation 关系表
    group_relation=models.ManyToManyField(Group)
    
class Args(models.Model):
    #测试 可空,不可空
    name=models.CharField(max_length=50,null=True)
    null_name=models.CharField(max_length=50,null=False)
    
class Assert(models.Model):
    hostname=models.CharField(max_length=50)
    #测试 创建时间 更新时间
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    
class Temp(models.Model):
    #测试choice
    GENDER_CHOICE=( (u'1',u'普通用户'),(u'2',u'管理员') ,(u'3',u'超级管理员') )
    gender=models.CharField(max_length=2,choices=GENDER_CHOICE)