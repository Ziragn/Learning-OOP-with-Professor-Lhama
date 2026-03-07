class MinhaClasse: #apartir de métodos, eu estou alterando um atributo que é privado
    def __init__(self):
        self.__valor = None
        self.__elem = None
    
    def setter_valor(self, valor: int) ->None :
        self.__valor = valor
    
    def getter_valor(self) ->int:
        return self.__valor

my_class = MinhaClasse()
#my_class.valor = 3 #ferindo o encapsulamento
my_class.setter_valor(42)
valor = my_class.getter_valor()
print(valor)

