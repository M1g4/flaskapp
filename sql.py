import sqlite3

with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")

    c.execute('INSERT INTO posts VALUES("Good", "I am good")')
    c.execute('INSERT INTO posts VALUES("Well", "I am well")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I am excellent")')
    c.execute('INSERT INTO posts VALUES("Okay", "I am okay")')


