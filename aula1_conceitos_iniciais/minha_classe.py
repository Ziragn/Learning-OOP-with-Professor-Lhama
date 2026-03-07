class MinhaClasse:
    def __init__(self,info, elem): #metodo construtor
        self.atributo_1 = 'meu atributo'
        self.atributo_2 = elem
        self.atributo_3 = [1,2,'a']
        self.new_atribute = info
        print(self.new_atribute)

    def metodo_1(self):
        print('minha ação1')
        print(self.atributo_2)
        return 'Olá Mundo'
    
    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo_3[1] + numero)


#objeto       #classe
minha_classe = MinhaClasse('info aqui no construtor', 213)
minha_classe.metodo_2(12)

#para casa abaixo:

class Pessoa:
    def __init__(self, altura:float, idade:int):
        self.altura = altura
        self.idade = idade
    
    def correr(self):
        print(f'Minha altura {self.altura} e {self.idade} idade e estou correndo')
    
    def comer(self):
        print(f'Minha altura {self.altura} e {self.idade} idade e estou comendo')

umberto = Pessoa(1.74, 31 )
umberto.correr()
umberto.comer()
