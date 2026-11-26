from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "team-availability-local-demo"
DATABASE = Path(__file__).with_name("team_availability.db")

INITIAL_USERS = [
    ("Alex Rivers", "Senior Developer", 1),
    ("Maya Chen", "UX Designer", 0),
    ("Jordan Taylor", "Project Manager", 1),
    ("Sofia Garcia", "Marketing Lead", 0),
    ("Noah Williams", "Backend Developer", 1),
    ("Ava Patel", "Data Analyst", 1),
]

def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS team_members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                available INTEGER NOT NULL DEFAULT 0 CHECK (available IN (0, 1))
            )
        """)
        count = connection.execute("SELECT COUNT(*) FROM team_members").fetchone()[0]
        if count == 0:
            connection.executemany(
                "INSERT INTO team_members (name, role, available) VALUES (?, ?, ?)",
                INITIAL_USERS
            )

@app.route("/")
def index():
    with get_connection() as connection:
        members = connection.execute(
            "SELECT id, name, role, available FROM team_members ORDER BY id"
        ).fetchall()
    available_count = sum(member["available"] for member in members)
    return render_template(
        "index.html",
        members=members,
        available_count=available_count,
        total_count=len(members)
    )

@app.route("/toggle/<int:member_id>", methods=["POST"])
def toggle_availability(member_id):
    with get_connection() as connection:
        member = connection.execute(
            "SELECT available FROM team_members WHERE id = ?",
            (member_id,)
        ).fetchone()

        if member is None:
            flash("Team member not found.", "error")
        else:
            new_status = 0 if member["available"] else 1
            connection.execute(
                "UPDATE team_members SET available = ? WHERE id = ?",
                (new_status, member_id)
            )
            flash("Availability updated successfully.", "success")

    return redirect(url_for("index"))

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
