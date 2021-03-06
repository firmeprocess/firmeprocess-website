import os, sys

# SET UP ENVIRONMENT
from common_functions import read_env, env_var
read_env()

# FLASK
from flask import Flask
from flask import render_template

app = Flask(__name__)

if env_var('ENVIRONMENT') == 'LOCAL':
    sys.stdout.write('\033[0;31m  >>  Running on LOCAL environment \033[0;0m\n')
    app.debug=True


### PROFILE ###

@app.route('/')
def home():
    return render_template('index.html', message="Welcome to *")


### Projects ###
@app.route('/projects')
def projects():
    return render_template('projects.html')


### PROFILE ###

@app.route('/about')
def about():
    return render_template('about.html')


### ABOUT ###

@app.route('/contact')
def contact():
    return render_template('contact.html')


### INFOGRAPHICS ###

@app.route('/infographics')
def infographics():
    return render_template('infographics/infographics.html')


@app.route('/infographics/daca')
def daca2014():
    return render_template('infographics/daca2014.html')


