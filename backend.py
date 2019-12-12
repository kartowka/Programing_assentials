import sqlite3

def connect():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists users(id INTEGER PRIMARY KEY,firstname text,lastname text,username text,password INTEGER,privilege INTEGER)")
    conn.commit()
    conn.close()

def insert(firstname,lastname,username,password,privilege):
    conn=sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO users VALUES(NULL,?,?,?,?,?)',(firstname,lastname,username,password,privilege))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(firstname="",lastname="",username=""):
    conn=sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE firstname=? OR lastname=? OR username=?",(firstname,lastname,username))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=?",(id,) )
    conn.commit()
    conn.close()

def update(id,firstname,lastname,username,password,privilege):
    conn=sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("UPDATE users SET firstname=?,lastname=?,username=?,password=? privilege=? WHERE id=?",(firstname,lastname,username,password,privilege,id))
    conn.commit()
    conn.close()

connect()
