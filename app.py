from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

#  DB Connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="esdrgt3456rev",   #  enter your password
        database="ums"
    )

#  Home → Register Page
@app.route('/')
def home():
    return render_template("register.html")

#  Register
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return render_template("login.html")   # 👈 direct login page

#  Login Page + Logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        return render_template("dashboard.html", email=email)
    else:
        return "Invalid Credentials "

#  Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

#  Run
if __name__ == '__main__':
    app.run(debug=True)