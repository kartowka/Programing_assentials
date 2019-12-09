import sqlite3
from tkinter import *
from admin import Admin
#from student import student
def connect():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists users(id INTEGER PRIMARY KEY,firstname text,lastname text,username text,password INTEGER,privilege INTEGER)")
    conn.commit()
    conn.close()

def check(username,password):
    conn=sqlite3.connect('database.db')
    cur = conn.cursor()
    if   (cur.execute('SELECT * FROM users WHERE username =? AND password = ?',(username,password))):
        if cur.fetchone():
            window = Tk()
            window.title('Admin_User')
            window.geometry('700x450')
            obj=Admin(window)
            window.mainloop()
        else:
            messagebox.showinfo('error','INVALID CREDENTIALS for ADMIN LOGIN')

# def checks(name,password):                       # for student login
#     conn=sqlite3.connect('login.db')
#     cur = conn.cursor()
#     if   (cur.execute('SELECT * FROM user WHERE name = ? AND password = ?', (name, password))):
#         if cur.fetchone():
#             window = Tk()
#             window.title('Student_User')
#             window.geometry('700x400')
#             obj = student(window)
#             window.mainloop()
#         else:
#             messagebox.showinfo('error','INVALID CREDENTIALS for STUDENT LOGIN')
#
#
#     conn.commit()
#     conn.close()

connect()
