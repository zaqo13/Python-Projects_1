import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port= 5432")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store1 (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port= 5432")
    cur=conn.cursor()
    # cur.execute("INSERT INTO store1 VALUES('%s','%s','%s')"%(item,quantity,price))  # '%s'== string formating placeholders #this will prone to SQL injections from attackers
    cur.execute("INSERT INTO store1 VALUES(%s,%s,%s)",(item,quantity,price)) # 2 arguments here seperated by quamms, 1st=sql querry, 2nd= variables
    conn.commit()   #above is only the right way to write sql queery without getting hacked!
    conn.close


def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port=5432")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store1")
    rows=cur.fetchall() #to fetch all data in variable, type is list()
    conn.close
    return rows

def delt(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port=5432")
    cur=conn.cursor()
    # cur.execute("DELETE FROM store WHERE item=?",(item,)) # cuomma at the end of item is needed!!!
    # cur.execute("DELETE FROM store1 WHERE item=%s"%(item))
    cur.execute("DELETE FROM store1 WHERE item=%s",(item,))
    conn.commit()
    conn.close

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port=5432")
    cur=conn.cursor()
    # cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s" %(quantity,price,item))
    cur.execute("UPDATE store1 SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close

# create_table()
#
# insert('apple', 7,120)
# # delt("apple")
# # update(15,360.0,"lime glass")
# print(view())

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
