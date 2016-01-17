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

