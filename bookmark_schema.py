import sqlite3

db = 'bookmark_db.sqlite'

def create_table():
# using a context manager to create the database
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS bookmarks (name text)') #TODO: figure out data types
    conn.close() # close at end of function


def display_all_data(): # does not require a context manager because you are not committing any changes
    
    bookmark_list = []
    
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products')
    for row in results:
        bookmark_list.append(row)

    return bookmark_list
    