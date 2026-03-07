class Mamifero:
    def __init__(self, localizacao:str) -> None:
        self.localizacao = localizacao
        self._tamanho = 1.23

    def andar(self) -> None:
        print(f'O Animal esta andando pelo {self.localizacao}')

    def _dormir(self) -> None: # Um único _ é método protegido. Acessível na propria classe, e também nas classes filhas
        print('O animal esta dormindo')



class Gato(Mamifero):
    def __init__(self, localizacao):
        super().__init__(localizacao)
    
    def miar(self) ->None:
        print('O gato esta miando ')
        self._dormir()

cat = Gato('Argentina')
cat.miar()
cat._dormir() #Deveria dar erro / elementos protegidos não são chamados por objetos
print(cat._tamanho) #mesma logica do de cima