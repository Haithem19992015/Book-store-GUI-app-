import sqlite3
# connection to a database
def connect():
    conn=sqlite3.connect('books.db')
    curs=conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT , author TEXT , year INTEGER , isbn INTEGER )")
    conn.commit()
    conn.close()
def insert(title,author,year,isbn):
    conn=sqlite3.connect('books.db')
    curs=conn.cursor()
    curs.execute("INSERT INTO book VALUES( NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect('books.db')
    curs=conn.cursor()
    curs.execute("SELECT * FROM book ")
    rows = curs.fetchall()
    conn.close()
    return rows

def search(title='',author='',year='',isbn=''):
    conn=sqlite3.connect('books.db')
    curs=conn.cursor()
    curs.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=curs.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect('books.db')
    curs = conn.cursor()
    curs.execute('DELETE FROM book WHERE id=?',(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect('books.db')
    curs=conn.cursor()
    curs.execute('UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?',(title,author,year,isbn,id))
    conn.commit()
    conn.close()
    
   
connect()
#insert()
#delete()
#update()
#view()
#search()


