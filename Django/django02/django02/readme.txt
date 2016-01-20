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

