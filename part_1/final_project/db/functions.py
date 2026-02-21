import sqlite3, os
from flask import jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
con = sqlite3.connect(os.path.join(BASE_DIR, "project.db"),check_same_thread=False)

cursor = con.cursor()




def select(columns,table, other=""):
    
    

    cursor.execute(f"SELECT {columns} FROM {table} {other}")
    
    
    return cursor.fetchall()

def insert(table, data):
    try:
        cursor.execute(f"INSERT INTO {table} {tuple(data.keys())} VALUES {tuple(data.values())}")
    except sqlite3.IntegrityError as e:
        return jsonify({'error': 'No book found'}), 400
    
def remove(table,condition):
    cursor.execute(f"DELETE FROM {table} WHERE {condition}")
    if cursor.rowcount == 0:
        return jsonify({'error': 'No book found'}), 400
    else:
        return jsonify({'status': 'ok'}), 200

def update(table,condition,changes):
    set_clause = ", ".join([f"{key} = '{value}'" for key, value in changes.items()])
    print(set_clause)
    print(f"UPDATE {table} SET {set_clause} WHERE {condition}")
    cursor.execute(f"UPDATE {table} SET {set_clause} WHERE {condition}")
    if cursor.rowcount == 0:
        return jsonify({'error': 'No book found'}), 400
    else:
        return jsonify({'status': 'ok'}), 200

### ALL 400 ARE PLACEHOLDERS, WILL BE WORKING ON IT TOMORROW :)

