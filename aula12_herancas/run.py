class Mamifero:
    def __init__(self, localizacao:str) -> None:
        self.localizacao = localizacao

    def andar(self) -> None:
        print(f'O Animal esta andando pelo {self.localizacao}')

class Cachorro(Mamifero): #Quando tem herança, todos os elementos públicos, que tem na classe de mamifero, vai ser passado para cachorro
    def __init__(self, localizacao:str):
        super().__init__(localizacao) #se refere ao construtor da classe superior

    def latir(self) ->None:
        print('O cachorro está latindo')
        self.andar()

class Gato(Mamifero):
    def __init__(self, localizacao):
        super().__init__(localizacao)
    
    def miar(self) ->None:
        print('O gato esta miando ')
        self.andar()

dog = Cachorro('brasil')
# dog.andar() #consegue utilizar os metodos públicos do outro 
# valor = dog.localizacao #consegue utilizar os atributos públicos do outro
# print(valor)
dog.latir()
cat = Gato('Noruega')
cat.miar()


# OBS: OS OBJETOS DAS CLASSES FILHAS, CONSEGUEM ACESSAR OS MÉTODOS DA CLASSE MÃE, MAS O CONTRÁRIO NÃO É POSSÍVEL.
#Diferença principal:

# Composição: A classe tem um objeto de outra classe como atributo e precisa chamar explicitamente os métodos dessa classe.

# Herança: A classe filha herda diretamente os métodos e atributos públicos da classe mãe, podendo usá-los sem a necessidade de instanciá-los.