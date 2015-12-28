#!/usr/bin/evn python
#coding=utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

if __name__=='__main__':
    app.run(debug = True)