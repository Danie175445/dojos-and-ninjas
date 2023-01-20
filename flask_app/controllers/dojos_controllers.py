from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo_model import Dojo

@app.route('/dojos')
def all_dojos():
    dojos_list = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos_list = dojos_list )

@app.route('/add_dojo', methods= ['post'])
def add_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojos_page(id):
    data ={
        'id': id
    }
    return render_template('dojos_show.html', dojo = Dojo.get_ninjas_in_dojos(data))
