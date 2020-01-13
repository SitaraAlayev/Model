import os
import sqlite3

DB_FILE = os.path.dirname(__file__) + '/login.db'
class Database:
    connection = -1
    def __init__(self):
        try:
            self.connection = sqlite3.connect(DB_FILE)
        except sqlite3.Error as e:
            print(e)
    
    def execute(self, statement):
        cur = self.connection.cursor()
        cur.execute(statement)
        return cur