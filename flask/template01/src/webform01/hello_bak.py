#!/usr/bin/evn python
#coding=utf-8

from flask import Flask,render_template,session,redirect,url_for,flash
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

app=Flask(__name__)
#设置通用密钥,一般建议把密钥写到配置文件中
app.config['SECRET_KEY']='hard to guess string'

class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('submit')
    
# @app.route('/',methods=['GET','POST'])
# def index():
#     name=None
#     form=NameForm()
#     if form.validate_on_submit():
#         name=form.name.data
#         form.name.data=''
#     return render_template('hello.html',form=form,name=name)

# @app.route('/',methods=['GET','POST'])
# def index():
#     name=None
#     form=NameForm()
#     if form.validate_on_submit():
#         session['name']=form.name.data
#         return redirect(url_for('index'))
#     return render_template('hello.html',form=form,name=session.get('name'))

@app.route('/',methods=['GET','POST'])
def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        old_name=session.get('name')
        if old_name is None and old_name !=form.name.data:
            flash('look like you have changed your name!')
        session['name']=form.name.data
        return redirect(url_for('index'))
    return render_template('hello.html',form=form,name=session.get('name'))

if __name__=='__main__':
    app.debug = True
    app.run()
    
    
    