import sqlite3

bookmark_list = []

db = 'bookmark_db.sqlite'
    
conn = sqlite3.connect(db)
results = conn.execute('SELECT * FROM bookmarks')
for row in results:
    bookmark_list.append(row)
conn.close()

print(bookmark_list)