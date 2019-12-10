import sqlite3
from tkinter import *
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
        result=cur.fetchone()
        return result

    conn.commit()
    conn.close()
        # if cur.fetchone():
        #     window = Tk()
        #     window.title('Admin_User')
        #     window.geometry('700x450')
        #     obj=Admin(window)
        #     window.mainloop()
        # else:
        #     messagebox.showinfo('error','INVALID CREDENTIALS for ADMIN LOGIN')

# def checks(username,password):                       # for student login
#     conn=sqlite3.connect('database.db')
#     cur = conn.cursor()
#     if   (cur.execute('SELECT * FROM users WHERE username = ? AND password = ? AND privilege==3', (username, password))):
#         if cur.fetchone():
#             window = Tk()
#             window.title('Student_User')
#             window.geometry('1400x500')
#             obj = student(window)
#             window.mainloop()
#         else:
#             messagebox.showinfo('error','INVALID CREDENTIALS for STUDENT LOGIN')
#



connect()
