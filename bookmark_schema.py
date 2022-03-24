import sqlite3

db = 'bookmark_db.sqlite'

def create_table():
# using a context manager to create the database
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS bookmarks (Name TEXT NOT NULL, Rating TEXT NOT NULL, Address TEXT NOT NULL, City TEXT NOT NULL, Telephone TEXT NOT NULL)') #TODO: figure out data types
    conn.close() # close at end of function

def insert_data(name, rating, address, business_city, telephone):
    with sqlite3.connect(db) as conn:
            conn.execute(f'INSERT INTO bookmarks VALUES (?, ?, ?, ?, ?)', (name, rating, address, business_city, telephone))
    conn.close()

def delete_data(yelpID):
    with sqlite3.connect(db) as conn:
        conn.execute(f'DELETE FROM bookmarks WHERE Name = ?', [yelpID])
    conn.close()

def display_all_data():
    
    bookmark_list = []
    
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM bookmarks')
    for row in results:
        bookmark_list.append(row)
    conn.close()

    return bookmark_list
    