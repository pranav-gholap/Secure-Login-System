from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import bcrypt
import os

app = Flask(__name__)

# Secret key for secure sessions
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-this")

DATABASE = "database/users.db"


# -----------------------------
# Database connection
# -----------------------------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# -----------------------------
# Create database and table
# -----------------------------
def init_db():
    os.makedirs("database", exist_ok=True)

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# Home page
# -----------------------------
@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# -----------------------------
# Registration
# -----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        # Basic validation
        if not username or not email or not password:
            flash("All fields are required.")
            return redirect(url_for("register"))

        if len(username) < 3:
            flash("Username must contain at least 3 characters.")
            return redirect(url_for("register"))

        if "@" not in email or "." not in email:
            flash("Please enter a valid email address.")
            return redirect(url_for("register"))

        if len(password) < 8:
            flash("Password must contain at least 8 characters.")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for("register"))

        # Hash password using bcrypt
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        conn = get_db_connection()

        try:
            # Parameterized query protects against SQL injection
            conn.execute(
                """
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
                """,
                (username, email, hashed_password.decode("utf-8"))
            )

            conn.commit()

        except sqlite3.IntegrityError:
            conn.close()
            flash("Username or email already exists.")
            return redirect(url_for("register"))

        conn.close()

        flash("Registration successful. Please log in.")
        return redirect(url_for("login"))

    return render_template("register.html")


# -----------------------------
# Login
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Email and password are required.")
            return redirect(url_for("login"))

        conn = get_db_connection()

        # Parameterized query
        user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        conn.close()

        if user and bcrypt.checkpw(
            password.encode("utf-8"),
            user["password"].encode("utf-8")
        ):
            session.clear()

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect(url_for("dashboard"))

        flash("Invalid email or password.")
        return redirect(url_for("login"))

    return render_template("login.html")


# -----------------------------
# Protected dashboard
# -----------------------------
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        flash("Please log in first.")
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


# -----------------------------
# Logout
# -----------------------------
@app.route("/logout")
def logout():

    session.clear()

    flash("You have been logged out.")

    return redirect(url_for("login"))


# -----------------------------
# Start application
# -----------------------------
if __name__ == "__main__":

    init_db()

    app.run(debug=True)