from cliente import Cliente
from cliente_DAO import ClienteDAO
from datetime import datetime

dao = ClienteDAO()

# Criar um novo cliente e salvar no banco
cliente1 = Cliente(
    idCliente=None,  # se for auto-incremento, use None
    nome='Maria Alves',
    tel='99999-0000',
    email='mariaalves@example.com',
    cidade='default',
    data_cadastro=datetime.now()  # data atual em python
)
dao.criar(cliente1)  # chama o método para inserir no banco

# Lista os clientes
clientes = dao.listar()
print("Listando os clientes")
for c in clientes:
    print(c)

# Atualiza os dados do primeiro cliente da lista
cliente1 = clientes[1]
cliente1.nome = 'Maria Alves'
cliente1.tel = '11111111'
cliente1.email = 'maria@gmail.com'
cliente1.cidade = 'Goiania'
cliente1.data_cadastro = datetime.now()

# Salva a atualização no banco
dao.atualizar(cliente1)

# Lista novamente para mostrar dados atualizados
clientes = dao.listar()
print('\nApós atualizar:')
for c in clientes:
    print(c)
