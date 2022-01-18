from flask import Flask, render_template, request, url_for, redirect, session, jsonify
import uuid
import pymongo
from passlib.hash import pbkdf2_sha256
from user.models import User
# from app import db

app = Flask(__name__)

#Data base e.g "MongoDB Compass"
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system #this name we will see in e.g. "MongoDB Compass"

# Create the user object
class User:

  def signup(self):
    print(request.form) #open 'User data' in terminal by VS code

# Personal data of user
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password')
    }
    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Chesk for existing email address
    if db.users.find_one({ "email": user['email'] }):
        return jsonify({"error": "Email address already in use"}), 400

    if db.users.insert_one(user): 
        return jsonify(user), 200

    return jsonify({ "error": "Signup failed" }), 400

# Routes
@app.route('/')  
def base():
    return render_template('base.html')

@app.route('/home/') 
def home():
    return render_template('home.html')

@app.route('/dashboard/') 
def dashboard():
    return render_template('dashboard.html')

@app.route('/user/signup/', methods=['POST'])
def signup():
    return User().signup()

app.run(port=5000)

if __name__ == "__main__":
  app.run(debug=True)


