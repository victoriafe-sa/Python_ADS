from conexao import criar_conexao, fechar_conexao

def insere_usuario(con, cod, nome_editora):
    cursor = con.cursor()
    sql = 'INSERT INTO editora(codeditora,nome_editora) VALUES (%s,%s)'
    valores = (cod, nome_editora)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()
    
def select_todas_editoras(con):
    cursor = con.cursor()
    sql = 'SELECT * FROM editora'
    cursor.execute(sql)
    
    for (codeditora, nome_editora) in cursor:
        print(codeditora,nome_editora)
    cursor.close()
    
def main():
    con = criar_conexao('localhost', 'root','','facsenac')
    select_todas_editoras(con)
    #insere_usuario(con, 16, 'Editora Moderna')
    fechar_conexao(con)
    
if __name__ == '__main__':
    main()