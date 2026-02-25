import sqlite3, os
from flask import jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
con = sqlite3.connect(os.path.join(BASE_DIR, "project.db"),check_same_thread=False)
con.row_factory = sqlite3.Row
cursor = con.cursor()

def select(columns,table, other=""):

    cursor.execute(f"SELECT {columns} FROM {table} {other}")
    
    rows = cursor.fetchall()
    
    return [dict(row) for row in rows]

def insert(table, data):

    try:
        cursor.execute(f"INSERT INTO {table} {tuple(data.keys())} VALUES {tuple(data.values())}")

        return cursor.rowcount
    
    except sqlite3.IntegrityError as e:     ## Integrity errors can be either because of unique constraint violation or null values in non-null columns
        if "UNIQUE constraint failed" in str(e):
            return 0
        return -1
    
    except sqlite3.OperationalError as e:
        return -1

    
def remove(table,condition):

    cursor.execute(f"DELETE FROM {table} WHERE {condition}")
    
    return cursor.rowcount

def update(table,condition,changes):

    set_clause = ", ".join([f"{key} = '{value}'" for key, value in changes.items()])
    cursor.execute(f"UPDATE {table} SET {set_clause} WHERE {condition}")

    return cursor.rowcount

