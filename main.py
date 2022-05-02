from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import false
from flask_login import UserMixin, LoginManager

required_start = "02.05.2022 12:29:00"
req_start_time = datetime.strptime(required_start, '%d.%m.%Y %H:%M:%S').timestamp()
req_end_time = datetime.strptime(required_start, '%d.%m.%Y %H:%M:%S')+timedelta(minutes=5)
req_end_time = req_end_time.timestamp()

app = Flask(__name__)
app.secret_key = "sprite"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = "sprite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# login = LoginManager(app)

# @login.user_loader
# def load_user(user_id):
#     return 

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.String(10), unique=True,nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    resp = db.Column(db.String(1000))

    def __init__(self,name,email,phone,topic):
        self.name = name
        self.email = email
        self.phone = phone
        self.topic = topic

class SecureModelView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            return False


admin = Admin(app)
admin.add_view(SecureModelView(users, db.session))

# while True:
#     found_user = users.query.filter_by(phone="9559978193").first()
#     if found_user:
#         print(found_user.resp)
#         print(found_user.phone)
#         db.session.delete(found_user)
#         db.session.commit()
#     else:
#         break
        
# while True:
#     found_user = users.query.filter_by(phone="09559978193").first()
#     if found_user:
#         db.session.delete(found_user)
#         db.session.commit()
#     else:
#         break

@app.route("/login/")
def login():
    session['logged_in'] = True
    return redirect("/admin/")

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        user = dict()

        user["name"] = request.form["name"]
        user["email"] = request.form["email"]
        user["phone"] = request.form["phone"]
        user["option"] = request.form["sel1"]
        

        found_user = users.query.filter_by(phone=user["phone"]).first()
        if found_user:
            flash(f"{user['phone']}") 
            return redirect(url_for("home"))
        else:
            usr = users(user["name"],user["email"],user["phone"],user["option"])
            db.session.add(usr)
            db.session.commit()

        # session["cur"] = user
        # return render_template("index.html", user = user)

        print(user["phone"])
        print(user["phone"])
        print("break")
        print("break")
        print("break")

        return redirect(url_for("wait", num=user["phone"]))


    else:
        # if "cur" in session:
        #     return redirect(url_for("write"))
        return render_template("home.html") 

@app.route('/wait/<num>')
def wait(num):
    return render_template("wait.html", num=num)

@app.route('/writing/<num>', methods=["POST","GET"])
def write(num):

    found_user = users.query.filter_by(phone=num).first()
    if request.method == "POST":
        cur_time = datetime.now().timestamp()
        if cur_time >= req_end_time:
            return render_template("timeout.html")
        user = request.form["ans"]
        found_user.resp = user
        db.session.commit()
        return render_template("success.html")

    
    if found_user:
        cur_time = datetime.now().timestamp()

        if cur_time >= req_start_time:
            return render_template("index.html", usr = found_user)
        else:
            return redirect(url_for("wait", num=num))
    else:
        print(num)
        print(num)
        print(num)
        return render_template("warn1.html")
    
    # if "cur" in session:
    #     usr = session["cur"]
    #     return render_template("index.html", usr = usr)
    # else:
    #     return redirect(url_for("home"))

@app.route('/terms/')
def Terms_and_conditions():
    return render_template("terms.html")


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