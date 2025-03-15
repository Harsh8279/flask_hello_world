from flask import Flask, render_template
from views import UserView

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secure-secret-key-here'    # when you work with forms, you need to set a secret key

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

UserView.register(app)

if __name__ ==  "__main__":
    app.run(debug=True)