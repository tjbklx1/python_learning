from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    print "==================="
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


if __name__=='__main__':
    app.run()
    # python template01 runserver --host 0.0.0.0