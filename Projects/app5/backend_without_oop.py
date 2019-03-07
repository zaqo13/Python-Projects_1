import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS book ( title text, author text, year integer, isbn integer )")
    conn.commit()
    conn.close

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.commit()
    conn.close
    return rows

def delete(title):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE title=?",(title,))
    conn.commit()
    conn.close

def update(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? where isbn=?",(title,author,year,isbn,isbn))
    conn.commit()
    conn.close

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
# delete("Grassland")
# update("Mahshoor vr 4.0", "Mr H", 1990, 21891732)   #update not working??? sqlite3.OperationalErroe: no such column: author
# insert('Mahshoor vr 1.0', 'Mr. Vanigya ', 1967, 23987)
# print(search(year=1967))
# insert('Mahshoor vr 2.0', 'Mr. Moreshwar ', 1913, 23982578)
# insert('Good columnspan', 'Mr. Unknow',2019, 237464)
# print(search("Mahshoor vr 4.0"))
# insert("Good columnspan","Mr. Unknow ",2019,3982689)
print(view())
