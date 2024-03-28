"СУБД - Система Управления Базой Данных"
"БД - База Данных"
"sqlite3"


import sqlite3

connection = sqlite3.connect("backend.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             full_name VARCHAR (30) NOT NULL,
             attendance DOUBLE (5 , 2) DEFAULT 0.0,
             hobby TEXT DEFAULT NULL,
             is_payment BOLEAN DEFAULT FALSE,
             birth_dste DATE
)""")

"int = INT, INTEGER, BIGINT"
"str = TEXT, VARCHAR"
"float = FLOAT, REAL, DOUBLE"
"bool = BOLEAN"
