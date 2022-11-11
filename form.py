from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    task_name = StringField('Nazwa zadania: ', [DataRequired()])
    date = StringField('Data: ')
    description = StringField('Opis: ', [DataRequired()])
