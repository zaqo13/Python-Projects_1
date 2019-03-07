import sqlite3
import json
from difflib import get_close_matches


class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute(" CREATE TABLE IF NOT EXISTS book ( title text, author text, year integer, isbn integer )")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows

    def delete(self,title):
        self.cur.execute("DELETE FROM book WHERE title=?",(title,))
        self.conn.commit()

    def update(self,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? where isbn=?",(title,author,year,isbn,isbn))
        self.conn.commit()

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows
    def __del__(self):
        self.conn.close()

class trans():
    def tr(w):
        data = json.load(open("076 data.json"))
        print("hi im in traslate")
        w = w.lower()
        if w in data:
            return data[w]


    # delete("Grassland")
    # update("Mahshoor vr 4.0", "Mr H", 1990, 21891732)   #update not working??? sqlite3.OperationalErroe: no such column: author
    # insert('Mahshoor vr 1.0', 'Mr. Vanigya ', 1967, 23987)
    # print(search(year=1967))
    # insert('Mahshoor vr 2.0', 'Mr. Moreshwar ', 1913, 23982578)
    # insert('Good columnspan', 'Mr. Unknow',2019, 237464)
    # print(search("Mahshoor vr 4.0"))
    # insert("Good columnspan","Mr. Unknow ",2019,3982689)
    # print(view())
