from flask import session, redirect, url_for

@app.route("/logout")
def logout():
    session.clear()   # Remove user session data
    return redirect(url_for("login"))
What it does:
✅ Clears the logged-in user's session
✅ Logs the user out securely
✅ Redirects back to the login page
Your project flow:
index.html
     |
     ↓
register.html
     |
     ↓
login.html
     |
     ↓
dashboard.html
     |
     ↓
logout → login.html