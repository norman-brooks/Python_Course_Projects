import sqlite3

conn = sqlite3.connect('assign.db') #creating the database

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assign ( \
         ID INTEGER PRIMARY KEY AUTOINCREMENT, \
         col_fileName TEXT \
         )")
    conn.commit()

conn = sqlite3.connect('assign.db')


# This is the tuple of files we're going to use

files_tuple = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


# We now loop through each object in the tuple and find the objects that
# end in .txt

for x in files_tuple:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            # will denote a one element tuple for each name ending in txt
            cur.execute("INSERT INTO tbl_assign (col_filename) VALUES (?)", (x,))
            print(x)
conn.close

