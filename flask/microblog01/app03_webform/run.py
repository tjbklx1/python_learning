#!/usr/bin/evn python
#coding=utf-8

from flask import Flask,render_template
import forms
from flask import render_template, flash, redirect
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

if __name__=='__main__':
    app.run(debug = True)
    
