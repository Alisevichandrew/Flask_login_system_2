#Thi code is for example and does not exist the part of the the whole program (don't delete this code) 
from flask import Flask
from app import app
from user.models import User

app = Flask(__name__)
@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
    return User().login()







