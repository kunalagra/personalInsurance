from flask import render_template, request
from app import app
from model import *


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/getPremium', methods=["POST"])
def getPremium():
    values = [request.form[k] for k in request.form]
    return calc_insurance(int(request.form['age']),float(request.form['bmi']),int(request.form['smoker']),int(request.form['gender']))

@app.route('/404', methods=["GET"])
def errorpage():
    return render_template("404.html")

@app.route('/about', methods=["GET"])
def blank():
    return render_template('about.html')

@app.route('/contact', methods=["GET"])
def contact():
    return render_template("contact.html")

@app.route('/service', methods=["GET"])
def service():
    return render_template('service.html')