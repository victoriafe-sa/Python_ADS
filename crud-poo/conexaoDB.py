import mysql.connector

class Conexao:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='senac',
            database='crud_poo',
        )
        self.cursor = self.conn.cursor()
    
    def fechar(self):
        self.cursor.close()
        self.conn.close()
