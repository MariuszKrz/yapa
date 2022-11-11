import base
from form import *
from flask import Flask, render_template, redirect, url_for
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SECRET_KEY'] = "uniquekey"

# strona glowna
@app.route('/')
def index():
	return render_template('index.html')

# Formularz dodawania zadania
@app.route('/dodaj', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    Session = sessionmaker(bind=base.engine)
    session = Session()

    if form.validate_on_submit():
        session.add(base.Terminarz(form.task_name.data, form.date.data, form.description.data))
        session.commit()

        return redirect(url_for("show_table"))
    return render_template('add_form.html', form=form)

# Tabela z zadaniami
@app.route('/table')
def  show_table():
    form = TaskForm()
    Session = sessionmaker(bind=base.engine)
    session = Session()

    records = session.query(base.Terminarz).all()

    return render_template('terminarz.html', form=form, records=records)

# Usuwanie zadan
@app.route('/delete<int:task_id>')
def delete_task(task_id):
	Session = sessionmaker(bind=base.engine)
	session = Session()
	session.query(base.Terminarz).filter(base.Terminarz.id==task_id).delete()
	session.commit()
	records = session.query(base.Terminarz).all()
	return render_template('terminarz.html', records=records)

#Edycja zadania
@app.route('/edit<int:task_id>', methods=['POST', 'GET'])
def edit_task(task_id):
	Session = sessionmaker(bind=base.engine)
	session = Session()
	form = TaskForm()
	



if __name__ == '__main__':
    app.run(debug=True)
