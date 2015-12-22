from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello Flask! I am %s </h1>' % name

if __name__=='__main__':
    app.run(debug=True)
    # http://127.0.0.1:5000/