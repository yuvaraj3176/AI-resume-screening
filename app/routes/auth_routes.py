from flask import Blueprint,render_template,request,redirect,session
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash

auth_bp = Blueprint("auth",__name__)

DB="instance/database.db"

@auth_bp.route("/login", methods=["POST"])
def login():

    username=request.form["username"]
    password=request.form["password"]
    role=request.form["role"]

    conn=sqlite3.connect(DB)
    cursor=conn.cursor()

    cursor.execute(
    "SELECT * FROM users WHERE username=? AND role=?",
    (username,role)
    )

    user=cursor.fetchone()

    conn.close()

    if user and check_password_hash(user[3],password):

        session["user"]=username
        session["role"]=role

        return redirect("/dashboard")

    return redirect("/")
@auth_bp.route("/register", methods=["POST"])
def register():

    username=request.form["username"]
    email=request.form["email"]
    password=generate_password_hash(request.form["password"])
    role=request.form["role"]

    conn=sqlite3.connect(DB)
    cursor=conn.cursor()

    cursor.execute(
    "INSERT INTO users(username,email,password,role) VALUES(?,?,?,?)",
    (username,email,password,role)
    )

    conn.commit()
    conn.close()

    return redirect("/")

@auth_bp.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html")
@auth_bp.route("/")
def home():

    return render_template("login.html")