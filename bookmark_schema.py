import sqlite3

db = 'bookmark_db.sqlite'

def create_table():
# using a context manager to create the database
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS bookmarks (Name TEXT NOT NULL, Rating TEXT NOT NULL, Address TEXT NOT NULL, City TEXT NOT NULL, Telephone TEXT NOT NULL)') #TODO: figure out data types
    conn.close() # close at end of function

def insert_data(yelpID):
    with sqlite3.connect(db) as conn:
        for name, rating, address, city, telephone in yelpID:
            conn.execute(f'INSERT INTO bookmarks VALUES (?, ?, ?, ?, ?)', (name, rating, address, city, telephone))
    conn.close()

def display_all_data(): # does not require a context manager because you are not committing any changes
    
    bookmark_list = []
    
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM bookmarks')
    for row in results:
        bookmark_list.append(row)
    conn.close()

    return bookmark_list
    