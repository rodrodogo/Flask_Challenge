from flask import Flask, request, render_template
from functions import *
import sqlite3

app =Flask(__name__)

@app.route('/')
def index():
	return app.send_static_file("index.html")
	#return Index.crt_person

@app.route('/search/<name>')
def search(name):
	i = users['name'].index(name)
	return '<h1>Hello %s!</h1><p>your age is %d</p>' % (name,users['age'][i])


@app.route('/insert', methods = ['POST'])
def insert():
	try:
		_name = request.form['firstname']
		_id = request.form['id']
		_age = request.form['age']
		conection = conectToDB()
		sql_gene = conection.cursor()
		sql_gene.execute("INSERT INTO person VALUES  ('{}', {}, {})".format(_name,_id,_age))
		#sql_gene.commit()
		#conection.close()
	except:
		name = ""


	return 'Hola {0}'.format(_name)

@app.route('/sout')
def sout():
	salida = ""
	conection = conectToDB()
	sql_gene = conection.cursor()
	for row in sql_gene.execute("SELECT * FROM person "):
		salida = salida + row
	conection.close()
	return salida



@app.route('/insertTeams', methods = ['POST'])
def insertTeams():
	try:
		name = request.form['firstname']

	except:
		name = ""


	return 'Hola {0}'.format(name)






app.run(debug=True)
