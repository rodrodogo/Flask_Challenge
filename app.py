from flask import Flask, request, render_template
from functions import *
import sqlite3

app =Flask(__name__)

@app.route('/')
def index():
	return app.send_static_file("crt_person.html")


@app.route('/insert', methods = ['POST'])
def insert():
	_age = request.form['age']
	_id = request.form['id']
	c = dbConector.getInstance()
	try:
		_name = request.form['firstname']
		c.insert("INSERT INTO person VALUES  ({2} ,'{0}', {1})".format(_name,_age,_id))
	except:
		_name = request.form['firstnameM']
		c.insert("UPDATE person SET name = '{0}', \
				age = {1} WHERE identification = {2}".format(_name,_age,_id))

	return 'Hola {0}'.format(_name)

@app.route('/vwPerson', methods = ['POST'])
def vwPerson():
	output = '''
				<table style="width:100%">
				  <tr>
				    <th>identification</th>
				    <th>name</th>
				    <th>Age</th>
				  </tr>
			'''
	_name = request.form['firstname']
	c = dbConector.getInstance()
	_result = c.query("SELECT * FROM person WHERE name = '{}'".format(_name))
	for row in _result:
		output += ''' <tr><th>{0}</th>
					<th>{1}</th>
					<th>{2}</th>
					</tr>
				'''.format(row['identification'],row['name'],row['age'])

	output += "</table>"
	return output

@app.route('/edtPerson', methods =['POST'])
def edtPerson():
	_name = request.form['firstname']
	c = dbConector.getInstance()
	_result = c.query("SELECT * FROM person WHERE name = '{}'".format(_name))
	output = '''
				<form action="/insert", method="post">
				  id:<br>
				  <input type="number" name="id"  value = "{0}"
				  readonly="readonly">
				  name:<br>
				  <input type="text" name="firstnameM"  value = "{1}">
				  <br>
				  age:<br>
				  <input type="number" name="age" value = "{2}">
				  <br><br>
				  <input type="submit" value="Submit">
				</form>
			'''.format(_result[0]['identification'],_result[0]['name'],_result[0]['age'])
	return output

@app.route('/rmvPerson', methods = ['POST'])
def rmvPerson():
	_id = request.form['id']
	c = dbConector.getInstance()
	c.insert("DELETE FROM person WHERE identification = {}".format(_id))
	return "Eliminado"


@app.route('/insertTeams', methods = ['POST'])
def insertTeams():
	try:
		name = request.form['firstname']

	except:
		name = ""


	return 'Hola {0}'.format(name)


app.run(debug=True)
