from flask import Flask, jsonify, render_template, request, redirect

server = Flask(__name__)

@server.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@server.route("/singin/", methods = ["GET", "POST"])
def singin():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        return redirect("/")
    
    return render_template("singin.html")

@server.route("/login/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        return redirect("/")

    return render_template("login.html")

server.run("0.0.0.0", 3030, debug=True)