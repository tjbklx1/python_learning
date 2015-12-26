#!/usr/bin/evn python
#coding=utf-8

from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    dic={'title':'blog','author':'valentine','date':'2015:06:25'}
    return render_template('testVarible03.html',dic=dic)

if __name__ == '__main__':
    app.debug = True
    app.run()