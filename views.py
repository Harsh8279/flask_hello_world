from flask_classful import FlaskView
from flask import render_template, jsonify
from forms import UserForm

class UserView(FlaskView):
    route_base = "/users"

    def __init__(self):
        super().__init__()
        self.users_data = [
            {
                "username": "Harsh",
                "email": "harsh.patel@gmail.com",
                "is_active": True
            },
            {
                "username": "Swayam",
                "email": "Swayam.patel@gmail.com",
                "is_active": True
            },
            {
                "username": "Hetarth",
                "email": "Hetarth.patel@gmail.com",
                "is_active": True
            },
            {
                "username": "Shivaay",
                "email": "Shivaay.patel@gmail.com",
                "is_active": True
            },
            {
                "username": "Yash",
                "email": "Yash.patel@gmail.com",
                "is_active": True
            },
            {
                "username": "Jash",
                "email": "Jash.patel@gmail.com",
                "is_active": True
            },
            {
                "username": "Vikrant",
                "email": "Vikrant.patel@gmail.com",
                "is_active": True
            },
            {
                "username": "Akshay",
                "email": "Akshay.patel@gmail.com",
                "is_active": True
            },
            {
                "username": "Kapil",
                "email": "Kapil.patel@gmail.com",
                "is_active": True
            },  
        ]
        

    def index(self):
        user_form = UserForm()
        return render_template("user_index.html",**{"users": self.users_data, "form": user_form})
    
    def get(self, username):
        for user in self.users_data:
            if user["username"] == username:
                return render_template("user_details.html", **user)
        
        return jsonify({"error": "User not found"}), 404
    
    def post(self):
        user_form = UserForm()
        if user_form.validate_on_submit():
            self.users_data.append({
                "username": user_form.username.data,
                "email": user_form.email.data,
                "is_active": True
            })
            return render_template("user_index.html", **{"users": self.users_data, "form": user_form})