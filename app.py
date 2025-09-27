from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# --- Database Setup ---
def init_db():
    conn = sqlite3.connect("messages.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --- Homepage Route ---
@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("messages.db")
    c = conn.cursor()

    if request.method == "POST":
        message = request.form.get("message")  # safer than direct indexing
        if message:  # only insert if not empty
            c.execute("INSERT INTO messages (content) VALUES (?)", (message,))
            conn.commit()
        conn.close()
        return redirect("/")  # refresh page to show new message

    # fetch all messages
    c.execute("SELECT content FROM messages ORDER BY id DESC")
    all_messages = c.fetchall()
    conn.close()

    return render_template("index.html", messages=all_messages)

# --- Run the app ---
if __name__ == "__main__":
    app.run(debug=True)
