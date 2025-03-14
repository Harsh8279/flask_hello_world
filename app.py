from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/user/<username>")
def hello_user(username):
    return render_template("greetings.html",
                           title="Greetings",
                           **{
                                 "username": username,
                                 "framework": "Flask"
                           }
                           )

if __name__ ==  "__main__":
    app.run(debug=True)