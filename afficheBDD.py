import sqlite3
conn = sqlite3.connect('bddSqlLite.db')
c = conn.cursor()
c.execute("SELECT * FROM connection")

for row in c.execute('SELECT * FROM connection ORDER BY rowId'):
        print row


conn.close()