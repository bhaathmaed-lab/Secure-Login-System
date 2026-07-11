from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Secure Login System</h1><p>Welcome to the project!</p>"

if __name__ == "__main__":
    app.run(debug=True)