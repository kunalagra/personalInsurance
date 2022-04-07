from cgitb import reset
import re
from urllib import response
from flask import render_template, request, redirect, url_for, session
from app import app
from model import *


@app.route('/', methods=["GET"])
def home():
    print(calc_insurance(36, 24, 0,1))
    return render_template('index.html')

@app.route('/getPremium', methods=["POST"])
def getPremium():
    values = [request.form[k] for k in request.form]
    print(values)

@app.route('/404', methods=["GET"])
def errorpage():
    return render_template("404.html")

# Blank Page


@app.route('/about', methods=["GET"])
def blank():
    return render_template('about.html')

# contact Page


@app.route('/contact', methods=["GET"])
def contact():
    return render_template("contact.html")

# service Page


@app.route('/service', methods=["GET"])
def service():
    return render_template('service.html')

# Charts Page

