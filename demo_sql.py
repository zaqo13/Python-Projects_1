import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store1 (item TEXT, quantity INTEGER,price REAL)")
    conn.commit()
    conn.close

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close


def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall() #to fetch all data in variable, type is list()
    conn.close
    return rows

def delt(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close

# insert("lime glass", 5,3)
# delt("water glasss")
update(8,25.0,"wine glass")
print(view())


"""
A programm that store this book info
Title, Auther
Year, ISBN

User can:

View all record
Search an entry
Add Entry
Update Entry
Delete Entry
Close
"""
