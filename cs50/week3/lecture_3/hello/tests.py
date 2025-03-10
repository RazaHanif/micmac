from django.test import TestCase

# Create your tests here.

# base file for vin decoder project

"""
Plan is to use the nhtsa api to create a vin decoder
have a webpage application
will use the finance project webpages as a template

first you need a proifle to use program
create user profiles that can save users cars
get user location for suggestions later

check page (home page) will give ability to punch in a vin and get info back,

maybe use carMD api to get users stored cars maintanice cycle info based on user provieded milage,

garage page stores cars, user can save cars to garage, provide estimated yearly milage (use that for maintance cycle predctions, add a function that weekly adds the predicted milage to the users car garage)
let user adjust car milage from garage page

email notication for car maintance???

link to guides or videos or somthing on how to do the maintance/service or like what/why you need to do it? idk check it out???
"sponsered" shops to contact to get the work done (just do canadian tire, jiffy lube, master mechanic and the dealer near the user)???


Build up the webpage and then after that using that as a base turn it into IOS app???

Dont forget ReadMe & Requirements txt
"""

import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """home page"""
    return apology("Homepage", 403)


@app.route("/vin", methods=["GET", "POST"])
@login_required
def vin():
    """vin check"""
    return apology("VIN CHECK page", 403)



@app.route("/garage")
@login_required
def garage():
    """Show user garage"""
    return apology("Garage", 403)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # Initalize values from form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # If any blank inputs, error
        if not username or not password or not confirmation:
            return apology("Input cannot be blank!")

        # If password and confirmation dont match, error
        if password != confirmation:
            return apology("Passwords do not match!")

        # if username already in database, error
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) > 0:
            return apology("Username already taken!", 400)
        else:
            key = generate_password_hash(password)
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, key
            )
            return render_template("login.html")
    else:
        return render_template("register.html")

@app.route("/shops", methods=["GET", "POST"])
@login_required
def shops():
    """ Show local shops """
    return apology("Shops", 403)


@app.route("/maintain", methods=["GET", "POST"])
@login_required
def maintain():
    """maintainance page"""
    return apology("maintainance", 403)

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code
