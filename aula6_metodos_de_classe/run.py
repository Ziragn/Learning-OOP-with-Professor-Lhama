class MinhaClasse:
    
    estatico = 'lhama'

    def __init__(self, estado) -> None:
        self.__estado = estado
    
    def print_variavel_de_classe(self):
        #print(estatico) não funciona, eu preciso colocar o self antes, para o python entender que tá dentro do contexto da classe
        print(self.estatico)
    
    # def alteracao_da_variavel_de_classe(self): #Aqui se cria um espelho, altera somente para o objeto.
    #     self.estatico = 'algumacoisa'

    @classmethod
    def alteracao_da_variavel_de_classe(cls): #Acessa a classe de forma geral
        cls.estatico = 'algumacoisa'



obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

# obj1.print_variavel_de_classe()
# obj1.alteracao_da_variavel_de_classe() # Aqui no caso alterou somente do obj1, como se fosse o espelho do exercicio anterior

# print(obj1.estatico)
# print(obj2.estatico)
# print(MinhaClasse.estatico)

obj1.alteracao_da_variavel_de_classe()
print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
