import sqlite3

conn = sqlite3.connect('db1.db',check_same_thread=False)
c = conn.cursor()


def authenticate(user_id, passwd):
    auth = 0
    users = get_users()
    for user in users:

        if (user_id, passwd) == (user[0], user[1]):
            auth = 1
            break
        else:
            if user_id not in user[0]:
                auth = 2
            else:
                auth = 0
    return auth; user_id


def get_users():
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    return users


def show_users(users):
    for user in users:
        print(user[0] + " " + user[1])


def insert_user(user_id, passwd):
    c.execute('INSERT INTO users VALUES(?,?)', (user_id, passwd))
    conn.commit()


