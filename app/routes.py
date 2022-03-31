from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, request, render_template, flash, redirect
from app import myobj
name="Lisa"
city_names=["Paris","London","Rome","Tahiti"]

class CityForm(FlaskForm):
    city = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@myobj.route("/", methods=['GET','POST'])
def home():
	form=CityForm()
	if form.validate_on_submit():
		flash('{0}'.format(form.city.data))
	return render_template('home.html',name=name,city_names=city_names,form=form)


