from flask import Flask, render_template, redirect, url_for, request, session
# from requests import request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        user = dict()

        user["name"] = request.form["name"]
        user["email"] = request.form["email"]
        user["phone"] = request.form["phone"]
        user["option"] = request.form["sel1"]


        # return render_template("index.html", user = user)

        return redirect(url_for("write", usr=user))

    else:        
        return render_template("home.html")

@app.route('/writing/')
def write():
    return render_template("index.html")


@app.route('/terms/')
def Terms_and_conditions():
    return "Terms and Conditions"

if __name__ == "__main__":
    app.run(debug=True)