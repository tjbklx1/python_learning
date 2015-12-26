from flask import Flask,render_template

app=Flask(__name__)

# mydict={'name':'tom','age':27,'addr':'beijing'}
# mylist=[1,2,3,4,5,6,7,8,9,0]
# 
# def getValue():
#     return "the return value"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

if __name__=='__main__':
    app.debug = True
    app.run()