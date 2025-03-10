from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "Frisbee"
]

REG = {}

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def reg():
    name = request.form.get("name") 
    sport = request.form.get("sport")
    if not name or sport not in SPORTS:
        return render_template("error.html")
    REG[name] = sport

    return render_template("register.html")

@app.route("/registered")
def registered():
    return render_template("registered.html", names=REG)