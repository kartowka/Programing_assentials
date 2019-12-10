import sqlite3



def connect():
    conn=sqlite3.connect("searchdatabase.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists question(id INTEGER PRIMARY KEY,questionSubject text,subQuestionSubject text,numberOfParagraphs text,difLvl text,terms text,year text,semester text,moed text,format text)")
    conn.commit()
    conn.close()

def insert(to_db):
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    cur.executemany('INSERT INTO question VALUES(NULL,?,?,?,?,?,?,?,?,?)',to_db)
    conn.commit()
    conn.close()

connect()