class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2*(self.largura + self.altura)
    
largura = float(input('Defina a largura: '))
altura = float(input('Defina a altura: '))

retangulo = Retangulo(largura, altura)
print(retangulo.calcular_area())
print(retangulo.calcular_perimetro())