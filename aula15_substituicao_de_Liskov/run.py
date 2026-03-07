# O Principio de Subs. de Liskov diz que objetos podem ser substituídos por seus subtipos(objetos filhos), sem que isso afete a execução correta do programa

# Quebra do principio:

class Animal:
    def alimentar(self):
        print('O animal está se alimentando')

class Cachorro(Animal):
    def latir(self):
        print('O cachorro esta latindo')

class Peixe(Cachorro):
    def nadar(self):
        print('O peixe esta nadando')
    
    def latir(self): # QUEBRA DO princípio: Ele diz que uma classe filha, pode em qlqqr circunstancia, substituir a execução da classe mãe. # comportamento diferente entre a classe mãe (cachorro) e a classe filha (Peixe)
        raise Exception('Peixe nao late') 
    
def verificar_animal(animal: any):
    animal.latir()

obj1 = Animal()
obj2 = Cachorro()
obj3 = Peixe()
verificar_animal(obj3)