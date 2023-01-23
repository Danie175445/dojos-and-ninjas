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

# @app.route('/edit_ninja')

@app.route('/delete_ninja/<int:ninja_id>/<int:dojo_id>')
def delete(ninja_id,dojo_id):
    data = {
        'id': ninja_id,
    }
    Ninja.delete(data)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/edit_ninja/<int:id>')
def edit_ninja(id):
    data = {
        'id': id
    }
    dojos_list = Dojo.get_all_dojos()
    ninja = Ninja.get_one(data)
    print('A')
    print(ninja)
    return render_template('edit_ninja.html',dojos_list = dojos_list, ninja = ninja)

@app.route('/update_ninja', methods = ['POST'])
def update_ninja():
    Ninja.edit(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f'/dojos/{dojo_id}')