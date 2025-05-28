class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
    
    def mostrar(self):
        print(f"O nome do aluno é {self.nome}, sua idade é {self.idade} e sua nota é {self.nota}")

aluno1 = Aluno('Paulo', 19, 9.9)
aluno1.mostrar()

aluno2 = Aluno(input('Digite seu nome: '), int(input('Digite sua idade: ')), int(input('Digite sua nota: ')))
aluno2.mostrar()