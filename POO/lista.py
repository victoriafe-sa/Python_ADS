#Exercicio 04 - Classe ContaBancaria com Encapsulamento
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente!")

    def exibir_saldo(self):
        print(f"Titular: {self.__titular} - Saldo: R${self.__saldo:.2f}")
# Teste
print('-----------------Exercicio 04-----------------')
conta = ContaBancaria("Maria", 1000)
conta.depositar(500)
conta.sacar(200)
conta.sacar(2000)  # Deve mostrar saldo insuficiente
conta.exibir_saldo()


#Exercicio 05 - Classe Aluno com Nota Final
class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def aprovado(self):
        return self.media() >= 7
# Teste
print('-----------------Exercicio 05-----------------')
aluno = Aluno("Lucas", 8.5, 6.5)
print(f"Média de {aluno.nome}: {aluno.media()}")
print("Aprovado?" , aluno.aprovado())


#Exercicio 06 - Herança – Funcionario e Gerente
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome} - Salário: R${self.salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Departamento: {self.departamento}")
# Teste
print('-----------------Exercicio 06-----------------')
func = Funcionario("João", 3000)
func.exibir_dados()

ger = Gerente("Ana", 5000, "TI")
ger.exibir_dados()


#Desafio 07 - Classe Produto com Estoque
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def vender(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
        else:
            print("Estoque insuficiente!")

    def repor(self, qtd):
        self.quantidade += qtd

    def exibir_estoque(self):
        print(f"{self.nome} - Preço: R${self.preco:.2f} - Estoque: {self.quantidade}")
# Teste
print('-----------------Exercicio 07-----------------')
produto = Produto("Mouse Gamer", 150.0, 10)
produto.exibir_estoque()
produto.vender(3)
produto.repor(5)
produto.vender(20)  # Estoque insuficiente
produto.exibir_estoque()