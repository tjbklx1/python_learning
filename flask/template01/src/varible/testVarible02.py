#!/usr/bin/evn python
#coding=utf-8

from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    user='valentine'
    nav_list=[u'首页',u'经济',u'文化',u'科技',u'娱乐']
    return render_template('testVarible02.html',username=user,nav_list=nav_list)

if __name__ == '__main__':
    app.debug = True
    app.run()