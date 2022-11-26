# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template
from app import app


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


@app.route('/login')
def login():
    print(1)
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)