import sqlite3
from tkinter import *
def connect():
    """function that connect to DB"""


    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists users(id INTEGER PRIMARY KEY,firstname text,lastname text,username text,password INTEGER,privilege INTEGER)")
    conn.commit()
    conn.close()

def check(username,password):
    """function that execute on the user by UserName and Password """



    conn=sqlite3.connect('database.db')
    cur = conn.cursor()
    if   (cur.execute('SELECT * FROM users WHERE username =? AND password = ?',(username,password))):
        result=cur.fetchone()
        return result

    conn.commit()
    conn.close()


connect()
