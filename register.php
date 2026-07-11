from flask import render_template, request, redirect
from werkzeug.security import generate_password_hash
from database import add_user
from utils import validate_password, validate_email, clean_input


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = clean_input(request.form["username"])
        email = clean_input(request.form["email"])
        password = request.form["password"]

        # Validate email
        if not validate_email(email):
            return "Invalid email format"

        # Validate password strength
        if not validate_password(password):
            return "Password must contain 8 characters, uppercase, lowercase, number and special character"

        # Hash password
        hashed_password = generate_password_hash(password)

        # Store user
        if add_user(username, email, hashed_password):
            return redirect("/login")
        else:
            return "User already exists"

    return render_template("register.html")
Your registration flow:
register.html
       |
       ↓
app.py (/register)
       |
       ↓
utils.py (validation)
       |
       ↓
database.py (store user)
       |
       ↓
users.db
For your Flask GitHub project, the correct files are:
templates/
 ├── register.html ✅
 └── login.html

app.py ✅
database.py ✅