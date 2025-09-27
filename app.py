from flask import Flask, render_template, request, redirect 
import sqlite3

app = Flask(__name__)

def init_db():
  conn = sqliite3.connect("messages.db")
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

@app.route("/", methods=["GET", "POST"])
def index():
  conn = sqlite3.connect("messages.db")
  c = conn.cursor()

if request.method == "POST":
  message = request.form["message"]
  c.execute("INSERT INTO messages (content) VALUES (?)", (message,))
  conn.commit()
  return redirect("/")

c.execute("SELECT content FROM messages")
all_messages = c.fetchall()
conn.close()

return render_template("index.html", messages=all_messages)

if __name__ = "__main__":
  app.run(debug=True)
