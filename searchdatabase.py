import sqlite3
def connect():
    conn=sqlite3.connect("searchdatabase.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists question(id INTEGER PRIMARY KEY,questionSubject text,subQuestionSubject text,numberOfParagraphs text,difLvl text,terms text,year text,semester text,moed text,format text)")
    conn.commit()
    conn.close()

def insertFromCSV(row):
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO question VALUES(NULL,?,?,?,?,?,?,?,?,?)',row)
    conn.commit()
    conn.close()
def insert(questionSubject,subQuestionSubject,numberOfParagraphs,difLvl,terms,year,semester,moed,format):
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO question VALUES(NULL,?,?,?,?,?,?,?,?,?)',(questionSubject,subQuestionSubject,numberOfParagraphs,difLvl,terms,year,semester,moed,format))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM question")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(questionSubject='',subQuestionSubject='',difLvl='',terms='',year='',semester='',moed='',format=''):
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM question WHERE questionSubject=? OR subQuestionSubject=? OR difLvl=? OR terms=? OR year=? OR semester=? OR moed=? OR format=?",(questionSubject,subQuestionSubject,difLvl,terms,year,semester,moed,format))
    #test field searh by questionSubject subQuestionSubject
    #cur.execute("SELECT * FROM question WHERE questionSubject=? OR subQuestionSubject=? ",(questionSubject,subQuestionSubject))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM question WHERE id=?",(id,) )
    conn.commit()
    conn.close()

def update(questionSubject,subQuestionSubject,numberOfParagraphs,difLvl,terms,year,semester,moed,format):
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    cur.execute("UPDATE question SET questionSubject=?,subQuestionSubject=?,numberOfParagraphs=?,difLvl=? ,terms=?,year=?,semester=?,moed=?,format=? WHERE id=?",(questionSubject,subQuestionSubject,numberOfParagraphs,difLvl,terms,year,semester,moed,format,id,))
    conn.commit()
    conn.close()

connect()
#issue()
#request()
