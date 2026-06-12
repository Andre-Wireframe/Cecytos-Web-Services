from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from flask_login import UserMixin, login_user, logout_user, login_required, current_user, LoginManager
import bcrypt
from bson import ObjectId

server = Flask(__name__)
server.secret_key = "admin123"

#User
class User(UserMixin):
    def __init__(self, id, name):
        self.id = id
        self.name = name

login_manager = LoginManager()
login_manager.init_app(server)

#Database
client = PyMongo(server, "mongodb://localhost:27017/cecytos_web")
db = client.db

def singin_back(name, password, password2):
    users_collection = db.users

    if password == password2:
        usersnames = users_collection.find({}, {"name":1}).to_list()
        if name in usersnames:
            print("Name in database")
            return "no_usr"
        else:
            hash_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(12))
            users_collection.insert_one(
                {
                    "name":name,
                    "password":hash_pw.decode("utf-8")
                })
            return True
    else:
        return "no_pass"

def login_back(name, password):
    users_collections = db.users
    user = users_collections.find({
        "name" : name
    }).to_list()[0]
    if user != []:
        if bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
            login_user(User(user["_id"], user["name"]))
            return True
        else:
            print("password_incorrect")
            return "no_pass"
    else:
        print("user_not_exits")
        return "no_usr"
    
def add_curse(titulo, descripcion, link):
    curses_collection = db.cursos
    curso_ch = curses_collection.find({"title":titulo}).to_list()

    if curso_ch[0] == []:
        return False

#Routes
@login_manager.user_loader
def load_user(id):
    user = db.users.find_one({"_id":ObjectId(id)})

    if user:
        return User(user["_id"], user["name"])
    else:
        return None

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
            return redirect(url_for("index"))
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
            return redirect(url_for("index"))
        else:
            context = {"errorcode":login_data}

    return render_template("login.html", **context)

@server.route("/cursos/<id>", methods = ["POST", "GET"])
@login_required
def cursos(id):
    context = {}
    if request.method == "POST":
        pass

server.run("0.0.0.0", 3030, debug=True)