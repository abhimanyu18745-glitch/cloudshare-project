from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CloudShare Running Successfully</h1>
    <a href='/login'>Go to Login Page</a>
    """

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
