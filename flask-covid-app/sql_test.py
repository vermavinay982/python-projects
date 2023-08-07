import sqlite3
# library to connect with sqlite3
# sqlite is connected with python 


"""
Relational databases allow for the
storage and retrieval of data, which
is stored in tables. Tables are similar
to spread sheets in that they have 
columns and rows—columns indicate 
what the data representes, such as “title” 
or “date.” Rows represent individual 
entries, which could be books, users,
transactions, or any other kind of entity.
"""
"""
The database we’re working with has
five columns id, published, author,
title, and first_sentence.
"""
# the db name with format .db
db_name='books.db'

# connection with database variable conn
conn = sqlite3.connect(db_name)

# cursor - that moves through the db to get data
cur = conn.cursor()

# the query to be done on the database
query = "select * from books"

# fetchall gives all the values from query
result = cur.execute(query).fetchall()

print(result)