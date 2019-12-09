import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL, password TEXT NOT NULL)")
        self.conn.commit()

    def insert(self,username,password):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO users VALUES(?,?)", (username,password))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()

        return rows

    def search(self,username=""):
        self.cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,username):
        self.cur.execute("DELETE FROM users WHERE username = ?", (username,))
        self.conn.commit()
        #conn.close()

    def update(self,username):
        self.cur.execute("UPDATE users SET username = ?, password = ?", (username,password))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()
