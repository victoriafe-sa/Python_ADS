import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'facsenac'
)

cursor = conexao.cursor()

#CRUD
#Update
nome_editora = "faculdade"
codeditora = 17
comando = "UPDATE editora SET nome_editora = %s WHERE codeditora = %s"

cursor.execute(comando, (nome_editora, codeditora))
#comando = update editora set nome_editora = 'MODERNA' Where codeditora = 13

conexao.commit() #edita o banco
cursor.close()
conexao.close()