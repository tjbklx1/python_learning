from flask import Flask
from flask import abort

app=Flask(__name__)

@app.route('/user/<id>')
def index(id):
    user=id
    if not user:
        abort(404)
    return '<h1>Hello %s</h1>' %user

if __name__=='__main__':
    app.run(debug=True)
    # http://127.0.0.1:5000/