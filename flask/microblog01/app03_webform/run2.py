#!/usr/bin/evn python
#coding=utf-8

from flask import Flask,render_template
import forms
from flask import render_template, flash, redirect
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')

@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',   
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title = 'Sign In',form = form)

@app.route('/login2', methods = ['GET', 'POST'])
def login2():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login2.html',title = 'Sign In',form = form)

@app.route('/login3', methods = ['GET', 'POST'])
def login3():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login3.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])
    
if __name__=='__main__':
    app.run(debug = True)
    
