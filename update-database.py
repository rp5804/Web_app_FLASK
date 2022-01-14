import sqlite3

conn = sqlite3.connect('db1.db')
c = conn.cursor()

#c.execute('DELETE FROM users WHERE user_id=""')
c.execute('SELECT * FROM users')
users = c.fetchall()
print(users)
conn.commit()
conn.close()