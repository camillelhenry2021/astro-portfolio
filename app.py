from datetime import timedelta

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True  # <--- makes the permanent session
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route("/admin")
def admin():
    return redirect(
        url_for("login")
    )  # url_for function takes an argument that is the name of the function that you want to redirect to


@app.route("/user")
def user():
    if "user" in session:
        usr = session["user"]
        return render_template("user.html", user=usr)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for_login)


if __name__ == "__main__":
    app.run()

# TO BE CONTINUED:  https://www.techwithtim.net/tutorials/flask/flask-adding-bootstrap
