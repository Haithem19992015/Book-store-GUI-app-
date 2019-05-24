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
#insert('But for me the show of this year 2019 is Babylon Berlin I will never forget the beautiful moments when I was watching this epic series yes liv lisa fries   ','cristiano ronaldo dos santos aveiro the game is over here, here we go  of the castles shine bright like a diamond in the sky this is what rihana and bryan cranston said in his sweet 60 birthday',2019,644234337)
#delete()
#update(9,'Kangarooo','Steve Harvey',2013,19992016)
#print(view())
#print(search( 'principles', 'Ray Dalio', 2016, 13213314))


