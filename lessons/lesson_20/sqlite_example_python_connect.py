import sqlite3

from constants import BASE_DIR
import random


try:
    connection = sqlite3.connect(BASE_DIR / 'sqlite_db.sqlite')

    print("DB was created!")

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS "user" (
	id NUMBER NOT NULL,
	name TEXT NOT NULL,
	description TEXT NULL,
	CONSTRAINT user_pk PRIMARY KEY (id)
);
""")

    cursor.execute(f"""INSERT INTO "user" ("id", "name") VALUES ({random.choice(range(400000))}, 'ALEX') """)
    connection.commit()

    cursor.execute("""SELECT * from user""")
    print(cursor.fetchall())



except Exception as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("SQLITE3 connection is closed")