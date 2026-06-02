from flask import Flask, jsonify, render_template, request, redirect
from flask_pymongo import PyMongo
from flask_login import UserMixin, login_user, logout_user
import bcrypt

server = Flask(__name__)

client = PyMongo(server, "mongodb://localhost:27017/cecytos_web")
db = client.db

def singin_back(name, password, password2):
    users_collection = db.users
    if password == password2:
        usersnames = users_collection.find({}, {"name":1}).to_list()
        if name in usersnames:
            print("Name in database")
            return "name_in_database"
        else:
            users_collection.insert(
                {
                    "name":name,
                    "password":password
                })
            return True
    else:
        return "bad_passwords"

def login_back(name, password):
    pass

@server.route("/", methods = ["GET"])
def index():
    context = {}
    return render_template("index.html", **context)

@server.route("/singin/", methods = ["GET", "POST"])
def singin():
    context = {}
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        singin_data = singin_back(name, password, password2)
        if singin_data == True:
            return redirect("/")
        else:
            context = {"errorcode":singin_data}
    
    return render_template("singin.html", **context)

@server.route("/login/", methods = ["GET", "POST"])
def login():
    context = {}
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        login_data = login_back(name, password)
        if login_data == True:
            return redirect("/")
        else:
            context = {"errorcode":login_data}

    return render_template("login.html", **context)

server.run("0.0.0.0", 3030, debug=True)