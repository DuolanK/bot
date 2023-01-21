import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('drf.db')
    cur = base.cursor()
    if base:
        print('DB connected!')
    base.execute('CREATE TABLE IF NOT EXISTS users(token TEXT, username TEXT PRIMARY KEY)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES (?,?)', tuple(data.values()))
        base.commit()
