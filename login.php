from flask import render_template, request, redirect, session
from werkzeug.security import check_password_hash
from database import get_user_by_email


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        # Find user from database
        user = get_user_by_email(email)

        if user:

            # Verify hashed password
            if check_password_hash(user["password"], password):

                session["user_id"] = user["id"]
                session["username"] = user["username"]

                return redirect("/dashboard")

        return "Invalid email or password"

    return render_template("login.html")
Login flow:
login.html
     |
     ↓
app.py (/login)
     |
     ↓
database.py (check user)
     |
     ↓
Password hash verification
     |
     ↓
dashboard.html