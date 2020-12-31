import sqlite3


db = sqlite3.connect("db.sqlite")
cursor = db.cursor()

# cursor.execute("""CREATE TABLE users(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     username TEXT,
#     email TEXT
#     )""")

# cursor.execute("INSERT INTO users VALUES(0,'Earnest Jacobs','Earnest_Jacobs','Earnest_Jacobs20@yahoo.com')")
# db.commit()

# user = (1, "John Smith", "John_Smith", "John_Smith@yahoo.com")
# cursor.execute("INSERT INTO users VALUES(?,?,?,?)", user)
# db.commit()

cursor.execute("DELETE FROM users WHERE id = 1")

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

for row in users:
    print(row)
