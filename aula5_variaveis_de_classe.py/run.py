class MinhaClasse:
    
    estatico = 'lhama'

    def __init__(self, estado) -> None:
        self.__estado = estado
        


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)
#print(obj1.estado) Não vai funcionar, pois o atributo está privado.

MinhaClasse.estatico = 'programador' # Todo mundo muda, os objetos que foram construidos antes da alteração, tbm recebem isso. É um elemento geral para todos
obj1.estatico = 'Ola, Mundo' # altera somente o objeto e não a classe toda.

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico) #contexto da classe consegue ser acessado, sem criar um objeto pra isso.
