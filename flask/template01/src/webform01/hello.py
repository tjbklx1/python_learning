#!/usr/bin/evn python
#coding=utf-8

from datetime import datetime

from flask import Flask,render_template,session,redirect,url_for,flash
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask.ext.script import Manager
from flask.ext.wtf import Form
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app=Flask(__name__)
#设置通用密钥,一般建议把密钥写到配置文件中
app.config['SECRET_KEY']='hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment=Moment(app)

class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500
    
@app.route('/',methods=['GET','POST'])
def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template('hello.html',form=form,name=name)

# @app.route('/',methods=['GET','POST'])
# def index():
#     name=None
#     form=NameForm()
#     if form.validate_on_submit():
#         session['name']=form.name.data
#         return redirect(url_for('index'))
#     return render_template('hello.html',form=form,name=session.get('name'))

# @app.route('/',methods=['GET','POST'])
# def index():
#     name=None
#     form=NameForm()
#     if form.validate_on_submit():
#         old_name=session.get('name')
#         if old_name is None and old_name !=form.name.data:
#             flash('look like you have changed your name!')
#         session['name']=form.name.data
#         return redirect(url_for('index'))
#     return render_template('hello.html',form=form,name=session.get('name'))

if __name__=='__main__':
    app.run(debug=True) 
    
# <form method="POST">
#     {{ form.hidden_tag() }}
#     {{ form.name.label }} {{ form.name() }}
#     {{ form.submit() }}
# </form>