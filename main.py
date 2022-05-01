from enum import unique
from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.String(10), unique=True,nullable=False, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    resp = db.Column(db.String(1000))

    def __init__(self,name,email,phone,topic):
        self.name = name
        self.email = email
        self.phone = phone
        self.topic = topic

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        user = dict()

        user["name"] = request.form["name"]
        user["email"] = request.form["email"]
        user["phone"] = request.form["phone"]
        user["option"] = request.form["sel1"]
        
        found_user = users.query.filter_by(phone="9559978193").first()
        if found_user:
            print("Yes")
            db.session.delete(found_user)
            db.session.commit()
        
        found_user = users.query.filter_by(phone="09559978193").first()
        if found_user:
            print("Yes")
            db.session.delete(found_user)
            db.session.commit()

        found_user = users.query.filter_by(phone=user["phone"]).first()
        if found_user:
            flash(f"This mobile number is already registered with {found_user.name}")
            return redirect(url_for("home"))
        else:
            usr = users(user["name"],user["email"],user["phone"],user["option"])
            db.session.add(usr)
            db.session.commit()

        # session["cur"] = user
        # return render_template("index.html", user = user)

        return redirect(url_for("wait", num=user["phone"]))

    else:
        # if "cur" in session:
        #     return redirect(url_for("write"))
        return render_template("home.html") 

@app.route('/wait/<num>')
def wait(num):
    return render_template("wait.html", number=num)

@app.route('/writing/')
def write():
    pass
    # if "cur" in session:
    #     usr = session["cur"]
    #     return render_template("index.html", usr = usr)
    # else:
    #     return redirect(url_for("home"))

@app.route('/terms/')
def Terms_and_conditions():
    return "Terms and Conditions"


# @app.route('/logout')
# def logout():
#     session.pop("cur",None)
#     return redirect(url_for("home"))


@app.route('/<other>')
def others(other):
    # if "cur" in session:
    #     return redirect(url_for("write"))
    # else:
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)