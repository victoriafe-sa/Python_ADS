import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'facsenac'
)

cursor = conexao.cursor()

#READ
comando = f'select * from editora'
cursor.execute(comando)
#conexao.commit() #edita o banco

resultado = cursor.fetchall() #ler o banco
print(resultado)
conexao.close()