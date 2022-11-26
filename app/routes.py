# -*- coding: utf-8 -*-
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template, flash, redirect, request
from app import app
con = sqlite3.connect("data/tenders_db.sqlite")
cur = con.cursor()
result = cur.execute("""SELECT * FROM experts
            WHERE is_super = 1""").fetchall()
print(result)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'miguel'}
    return render_template('base.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        flash('Регистрация успешна')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
