import sqlite3

# Establish a connection to a database
db = sqlite3.connect("db.sqlite")

# Create a cursor object to execute SQLite commands.
cursor = db.cursor()

# Create a users table
cursor.execute("""CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT
    )""")

# Add a user to the table and commit these changes to the database
cursor.execute("INSERT INTO users VALUES(0,'Earnest Jacobs','Earnest_Jacobs','Earnest_Jacobs20@yahoo.com')")
db.commit()

# Add another user to the table
# This time we use placeholders instead of writing data directly into sql queries
user = (1, "John Smith", "John_Smith", "John_Smith@yahoo.com")
cursor.execute("INSERT INTO users VALUES(?,?,?,?)", user)
db.commit()

# Delete data from the table
cursor.execute("DELETE FROM users WHERE id = 1")

# Run a select statment to get data from the users table
cursor.execute("SELECT * FROM users")
# We have to call fetchall() method to retrieve data from the database
# It will return a list
users = cursor.fetchall()


# Loop through the list and print each row
for row in users:
    print(row)
