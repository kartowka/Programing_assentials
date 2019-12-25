import sqlite3
def connect():
    conn=sqlite3.connect("searchdatabase.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists question(id INTEGER PRIMARY KEY,questionSubject text,subQuestionSubject text,numberOfParagraphs text,difLvl text,terms text,year text,semester text,moed text,format text)")
    cur.execute("CREATE TABLE if NOT exists numberOfParagraphs(id INTEGER PRIMARY KEY,q1 REAL,q2 REAL,q3 REAL,q4 REAL,q5 REAL,q6 REAL,q7 REAL,q8 REAL,q9 REAL,q10 REAL,numberOfRaters INTEGER)")
    conn.commit()
    conn.close()

def insertFromCSV(row):
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO question VALUES(NULL,?,?,?,?,?,?,?,?,?)',row)
    cur.execute('INSERT INTO numberOfParagraphs VALUES(NULL,0,0,0,0,0,0,0,0,0,0,0)')
    conn.commit()
    conn.close()

def insert(questionSubject,subQuestionSubject,numberOfParagraphs,difLvl,terms,year,semester,moed,format):
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO question VALUES(NULL,?,?,?,?,?,?,?,?,?)',(questionSubject,subQuestionSubject,numberOfParagraphs,difLvl,terms,year,semester,moed,format))
    cur.execute('INSERT INTO numberOfParagraphs VALUES(NULL,0,0,0,0,0,0,0,0,0,0,0)')
    conn.commit()
    conn.close()

def updateRating(id,q1='',q2='',q3='',q4='',q5='',q6='',q7='',q8='',q9='',q10=''):
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    #cur.execute('INSERT INTO question VALUES(NULL,?,?,?,?,?,?,?,?,?)',(questionSubject,subQuestionSubject,numberOfParagraphs,difLvl,terms,year,semester,moed,format))
    cur.execute("UPDATE numberOfParagraphs SET q1=?,q2=?,q3=?,q4=?,q5=?,q6=?,q7=?,q8=?,q9=?,q10=?,numberOfRaters = numberOfRaters + 1 WHERE id=?",(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,id,))
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
    rows=cur.fetchall()
    conn.close()
    return rows

def getNumberOfRaters(id):
    conn=sqlite3.connect('searchdatabase.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM numberOfParagraphs WHERE id=? ",(id,))
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
