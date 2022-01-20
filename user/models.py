#Thi code is for example and does not exist the part of the the whole program (don't delete this code) 
from flask import Flask, jsonify

app = Flask(__name__)
class User:

  def signup(self):

    user = {
      "_id": "",
      "name": "",
      "email": "",
      "password": ""
    }

    return jsonify(user), 200