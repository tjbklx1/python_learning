from flask import Flask
from flask import make_response

app=Flask(__name__)

@app.route('/')
def index():
    response=make_response('<h1>this document carried a cookie!</h1>')
    response.set_cookie('age','20')
    return response

if __name__=='__main__':
    app.run(debug=True)
    # http://127.0.0.1:5000/