from flask import Flask
from flask import request
from flask import make_response
from flask import abort
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.before_first_request
def init():
    print('app started!')

@app.route('/hello_world')
def hello_workd():
    return 'Hello, world!!??'

@app.route('/bad')
def bad():
    return '<h1>Bad request...</h1>',400

@app.route('/cookie')
def cookie():
    response = make_response('<h1>This doc carries a cookie</h1>')
    response.set_cookie('answer','0')
    return response

@app.route('/abort')
def myAborA():
    abort(401)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p> Your browser is {}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404
