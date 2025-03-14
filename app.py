from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/user/<username>")
def hello_user(username):
    return f"<h1>Hello, {username}! Flask this side.</h1>"

if __name__ ==  "__main__":
    app.run(debug=True)