#!/usr/bin/evn python
#coding=utf-8

TEMPLATE_DEBUG=True
TEMPLATE_DIRS=(os.path.dirname(BASE_DIR,'templates'),)

STATIC_URL = '/static/'
STATICFILES_DIRS=(os.path.dirname(BASE_DIR,'static'),)

v1.8
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

记住是join

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webdb',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}


from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^company/', include('company.urls')),
]

is_empty=all([user,pwd])


后台传递HTML标签
from django.utils.safestring import mark_safe
page=mark_safe("<a href='/company/host/1'>1</a>")




session 

Browser-Length Sessions vs. Persistent Sessions

You might have noticed that the cookie Google sent us 
at the beginning of this chapter contained expires=Sun, 17-Jan-2038 19:14:07 GMT;. 
Cookies can optionally contain an expiration date that advises the browser on when to remove the cookie. 
If a cookie doesn’t contain an expiration value, the browser will expire it when the user closes his or her browser window. 
You can control the session framework’s behavior in this regard with the SESSION_EXPIRE_AT_BROWSER_CLOSE setting.

By default, SESSION_EXPIRE_AT_BROWSER_CLOSE is set to False, 
which means session cookies will be stored in users’ browsers for SESSION_COOKIE_AGE seconds 
(which defaults to two weeks, or 1,209,600 seconds).
Use this if you don’t want people to have to log in every time they open a browser.

If SESSION_EXPIRE_AT_BROWSER_CLOSE is set to True, Django will use browser-length cookies.



insert into company_assert (hostname, ip, user_group_id) values('test1','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test2','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test3','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test4','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test5','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test6','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test7','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test8','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test9','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test10','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test11','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test12','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test13','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test14','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test15','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test16','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test17','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test18','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test19','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test20','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test21','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test22','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test23','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test24','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test25','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test26','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test27','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test28','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test29','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test30','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test31','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test32','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test33','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test34','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test35','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test36','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test37','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test38','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test39','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test40','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test41','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test42','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test43','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test44','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test45','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test46','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test47','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test48','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test49','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test50','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test51','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test52','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test53','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test54','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test55','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test56','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test57','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test58','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test59','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test60','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test61','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test62','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test63','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test64','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test65','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test66','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test67','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test68','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test69','1.1.1.1','1');
insert into company_assert (hostname, ip, user_group_id) values('test70','1.1.1.1','1');


