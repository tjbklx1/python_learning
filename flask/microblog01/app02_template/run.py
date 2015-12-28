#!/usr/bin/evn python
#coding=utf-8

# template 

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return '''
            <html>
              <head>
                <title>Home Page</title>
              </head>
              <body>
                <h1>Hello, ''' + user['nickname'] + '''</h1>
              </body>
            </html>
        '''
    
@app.route('/index2')
def index2():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index2.html", title = 'Home', user = user)

@app.route('/index3')
def index3():
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
    return render_template("index3.html",
        title = 'Home',    # optional
        user = user,
        posts = posts)
    
@app.route('/index4')
def index4():
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
    return render_template("index4.html",
        title = 'Home',    # optional
        user = user,
        posts = posts)
    
@app.route('/index5')
def index5():
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
    return render_template("index5.html",
        title = 'Home',   
        user = user,
        posts = posts)

if __name__=='__main__':
    app.run(debug = True)