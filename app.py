from flask import Flask

app =Flask(__name__)

usuarios = {'nombre' : ['carlos', 'rodrigo'], 'edad': [22 , 19]}

@app.route('/')
def index():
	print (usuarios['nombre'])
	return '<h1>Hello!</h1>'

@app.route('/otro/<name>')
def otro(name):
	return '<h1>Hello {}!</h1>'. format(name)