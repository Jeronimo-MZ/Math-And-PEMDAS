import sqlite3

class User:

    def __init__(self):
        self.conn = sqlite3.connect("Users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Users(Id INTEGER PRIMARY KEY, Name TEXT, Points INTEGER)')


