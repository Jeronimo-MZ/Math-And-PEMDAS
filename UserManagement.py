import sqlite3

class User:

    def __init__(self):
        self.user_id = None
        self.conn = sqlite3.connect("Users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Users(Id INTEGER PRIMARY KEY,\
        Name TEXT UNIQUE NOT NULL, Points INTEGER NOT NULL)')
        self.name = ''
        self.points = 0
    

    def addUser(self, name, points=0):
        name:str = name.title()
        self.user_id = 1
        self.cursor.execute('SELECT * FROM Users')
        users = self.cursor.fetchall()
        # print(users)
        if len(users) > 0:
            self.user_id = users[-1][0] + 1
        # print(id_num)
        self.cursor.execute(f"INSERT INTO Users VALUES({self.user_id}, '{name}', {points})")
        self.name = name
        self.points = points
        self.save()

    def search(self, userName):
        userName = userName.title()
        self.cursor.execute('SELECT * FROM Users')
        users = self.cursor.fetchall()
        for user in users:
            if user[1] == userName:
                return user[1]
        return None
    
    def getUserData(self, name):
        self.cursor.execute('SELECT * FROM Users')
        users = self.cursor.fetchall()
        for user in users:
            if user[1] == name:
                self.name = user[1]
                self.points = user[-1]
                self.user_id = user[0]
        return (self.user_id, self.name, self.points)

    def updateScore(self, points):
        self.points = points
        self.cursor.execute(f"UPDATE Users SET points={points}  WHERE id={self.user_id}")
        self.save()
    
    def showUsers(self):
        self.cursor.execute('SELECT * FROM Users')
        users = self.cursor.fetchall()
        [print(user) for user in users]
    
    def getScore(self, user_name):
        return self.getUserData(user_name)[-1]

    def save(self):
        self.conn.commit()
    
    def close(self):
        self.conn.close()
    
if __name__ == "__main__":
    usuario = User()
    usuario.addUser('John')
    usuario.showUsers()
    usuario.save()
    usuario.close()