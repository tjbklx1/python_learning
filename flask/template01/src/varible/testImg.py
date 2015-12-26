#!/usr/bin/evn python
#coding=utf-8

from flask import Flask, render_template, url_for
app = Flask(__name__)
 
@app.route('/')
def index():
    img = url_for('static', filename='imgs/cat.jpg')
    return render_template('img.html',img=img)

if __name__ == '__main__':
    app.debug = True
    app.run()