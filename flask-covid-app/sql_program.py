import sqlite3

# the db name with format .db
db_name='books.db' # todo.db bhi aa skta hai yaha

# connection with database variable conn
conn = sqlite3.connect(db_name) # us db me ghus gaye is se

# cursor - that moves through the db to get data
cur = conn.cursor() # just like our cursor in excel
query = "select * from books" # sql query simple wali

while True:
	query=input("Type your Query\n") #input leli user se
	# fetchall gives all the values from query
	try:
		result = cur.execute(query).fetchall() # execute karke result lelia
		print(result)
	except Exception as e:
		print("Wrong Query - "+str(e)+"\n") # if error aaya to batado band mar karo par
