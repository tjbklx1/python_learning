from flask import Flask
from flask.globals import request

app=Flask(__name__)

@app.route('/')
def index():
    user_agent=request.headers.get('User-Agent')
    return '<p>Your browser is : %s </p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello Flask! I am %s </h1>' % name

if __name__=='__main__':
    app.run(debug=True)
    # http://127.0.0.1:5000/