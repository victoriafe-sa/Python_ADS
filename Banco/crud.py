import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'facsenac',
    port = '3306'
)

cursor = conexao.cursor()
#cursor.close()
#conexao.close()

#CRUD
cod = 53 
nome_editora = 'senac'

comando = f'INSERT INTO editora(codeditora, nome_editora) values ({cod}, "{nome_editora}")'
cursor.execute(comando)
conexao.commit() #edita o banco

#resultado = cursor.fetchall() #ler o bancop