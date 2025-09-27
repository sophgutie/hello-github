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

