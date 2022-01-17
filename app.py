from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)

@app.route('/')  
def base():
    return render_template('base.html')

@app.route('/home/') 
def home():
    return render_template('home.html')

@app.route('/dashboard/') 
def dashboard():
    return render_template('dashboard.html')

app.run(port=5000)

