import sqlite3
import os

conn = sqlite3.connect('test.db')

print("Opened database successfully")

def execute_command(query) -> None:
    try:
        #with sqlite3.connect('test.db') as conn:
        result = conn.execute(query)
        print(f"El comando se ejecutó correctamente. {result.rowcount}")
        conn.rollback()
        conn.commit()
    except Exception as ex:
        raise

def execute_reader(query: str) -> tuple:
    cursor = conn.execute(query)
    for item in cursor:
        yield item

query = '''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL);'''
#execute_command(query)

query = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Paul', 32, 'California', 20000.00 )"
execute_command(query)

query = 'SELECT * from COMPANY'
for r in execute_reader(query):
    print(r)