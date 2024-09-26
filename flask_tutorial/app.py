import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "wow so secret!"


def connect_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        conn = connect_db()
        note_id = request.form["note_id"]
        conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
        conn.close()
        flash("Note was successfully deleted!")
    # Initiate a connection to the database
    conn = connect_db()

    # Run SQL Query to retrieve all notes
    notes = conn.execute("SELECT * FROM notes").fetchall()

    # Close the connection when done, good practice
    conn.close()

    return render_template("index.html", notes=notes)


@app.route("/create", methods=("GET", "POST"))
def create_note():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]

        if not title or not description:
            flash("Title and description are required!")
        else:
            conn = connect_db()
            conn.execute(
                "INSERT INTO notes (title, description) VALUES (?, ?)",
                (title, description),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("create.html")
