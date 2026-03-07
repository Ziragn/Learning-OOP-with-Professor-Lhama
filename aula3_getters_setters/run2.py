class MinhaClasse: #apartir de métodos, eu estou alterando um atributo que é privado
    def __init__(self):
        self.__valor = None
        self.__elem = None
    
    def setter_valor(self, valor: int) ->None : #Obs: Esse int aqui, é somente para o outro usuario/programador, entender q quero um int aqui, mas ele não interfere na programação em si do programa.
        self.__valor = valor
        
    @property
    def getter_valor(self) ->int:
        return self.__valor

my_class = MinhaClasse()
my_class.setter_valor(123)
print(my_class.getter_valor) # esse property permite a olhar um método , como se fosse atributo da nossa classe.