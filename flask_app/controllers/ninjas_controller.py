from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/add_ninja')
def add_ninja():
    dojos_list = Dojo.get_all_dojos()
    return render_template('new_ninja.html', dojos_list = dojos_list)

@app.route('/creat_ninja', methods= ['POST'])
def creat_ninja():
    Ninja.save(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')