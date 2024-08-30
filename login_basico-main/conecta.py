import mysql.connector
from usuario import Usuario

class DatabaseConnection:
    def __init__(self) -> None:
        self.user = "root"
        self.password = ""
        self.database = "proyecto_ppi"
        self.host = "localhost"

    def open(self):
        self.conn = mysql.connector.connect(host = self.host,
                                            user = self.user,
                                            passwd = self.password,
                                            database = self.database)
        return self.conn
    
    def close(self):
        self.conn.close()