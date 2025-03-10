import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    """Show portfolio of stocks"""
    users = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    name = users[0]["username"].title()
    cash = float(users[0]["cash"])
    total = cash

    """Get the portfolio, summing values for amount while disregarding all 0 on hand stocks"""
    shares = db.execute(
        "SELECT stock, SUM(amount), price FROM shares WHERE user_id = ? GROUP BY stock HAVING amount > 0",
        session["user_id"],
    )
    for row in shares:
        row["SUM(amount)"] = float(row["SUM(amount)"])
        row["price"] = float(current_price(row["stock"]))
        total += row["price"]

    return render_template(
        "index.html", name=name, cash=cash, share=shares, total=total
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        ticker = request.form.get("symbol")
        shares = request.form.get("shares")

        stock = lookup(ticker)
        if not stock:
            return apology("Invalid Symbol")

        try:
            shares = int(shares)
        except:
            return apology("Shares must be a number")

        if not shares > 0:
            return apology("Shares must be a positive number")

        """Get current Cash on hand to determine if user has enough funds aswell as update later"""
        row = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash_onhand = float(row[0]["cash"])
        cost = shares * float(stock["price"])
        if cost > cash_onhand:
            return apology("Insufficient Funds!")

        db.execute(
            "INSERT INTO shares (user_id, stock, price, amount, date_time) VALUES (?, ?, ?, ?, ?)",
            session["user_id"],
            stock["symbol"],
            stock["price"],
            shares,
            datetime.now(),
        )
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?",
            (cash_onhand - cost),
            session["user_id"],
        )
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    shares = db.execute("SELECT * FROM shares WHERE user_id = ?", session["user_id"])
    return render_template("history.html", share=shares)


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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        ticker = request.form.get("symbol")
        stock = lookup(ticker)
        if not stock:
            return apology("Invalid Symbol")
        else:
            return render_template("quoted.html", stock=stock)
    else:
        return render_template("quote.html")


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


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        ticker = request.form.get("symbol")
        num = request.form.get("shares")

        if not ticker:
            return apology("Invalid Symbol")

        stock = lookup(ticker)

        try:
            num = int(num)
        except:
            return apology("Shares must be a positive number")

        if not num > 0:
            return apology("Shares must be a positive number")

        """Check if user has enough money, also to update later"""
        row = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash_onhand = float(row[0]["cash"])
        change = num * float(stock["price"])

        rows = db.execute(
            "SELECT SUM(amount) FROM shares WHERE user_id = ? AND stock = ? GROUP BY stock HAVING sum(amount) > 0",
            session["user_id"],
            ticker,
        )
        amount = float(rows[0]["SUM(amount)"])

        if num <= amount:
            db.execute(
                "INSERT INTO shares (user_id, stock, price, amount, date_time) VALUES (?, ?, ?, ?, ?)",
                session["user_id"],
                stock["symbol"],
                stock["price"],
                -abs(num),
                datetime.now(),
            )
            db.execute(
                "UPDATE users SET cash = ? WHERE id = ?",
                (cash_onhand + change),
                session["user_id"],
            )
            return redirect("/")
        else:
            return apology("Insufficient amount of shares")

    else:
        shares = db.execute(
            "SELECT stock, SUM(amount) FROM shares WHERE user_id = ? GROUP BY stock HAVING sum(amount) > 0",
            session["user_id"],
        )
        return render_template("sell.html", names=shares)


def current_price(tick):
    symbol = lookup(tick)
    return symbol["price"]
