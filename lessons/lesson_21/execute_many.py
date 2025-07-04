import sqlite3

from constants import BASE_DIR
import random



connection = sqlite3.connect(BASE_DIR / 'sqlite_db.db')
cur = connection.cursor()


# cur.execute(
# """INSERT INTO "user" ("id", "name") VALUES (?, ?)""", ((100, 'Olol'), (200, 'aaa'), (300, 'Den'))
# )

cur.execute("""select * from "user" """)
print(cur.fetchall())
cur.executemany(
f"""INSERT INTO "user" ("id", "name") VALUES (?, ?) """,
    [(102, 'Olol'), (202, 'aaa'), (302, 'Den')]
)

connection.commit()
connection.close()