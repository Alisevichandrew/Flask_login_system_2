from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from user.models import User

app = Flask(__name__)
# Create the user object
class User:

  def signup(self):

    user = {
      "_id": "",
      "name": "",
      "email": "",
      "password": ""
    }

    return jsonify(user), 200

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

@app.route('/user/signup/', methods=['GET'])
def signup():
    return User().signup()

app.run(port=5000)

if __name__ == "__main__":
  app.run(debug=True)


