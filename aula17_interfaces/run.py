from abc import ABC, abstractmethod
#declarar classe abstrata/ método abstrato

class Trabalhador(ABC): #classe abstrata , composta somente por métodos abstratos, em python a gente toma isso como uma interface.
#interface > É uma pré assinatura, uma ideia que a gente tem de construção de uma classe atuante.

    @abstractmethod
    def trabalhar(self):
        pass

    @abstractmethod
    def ir_para_casa(self):
        pass

    @abstractmethod
    def horario_de_almoco(self):
        pass

class Professor(Trabalhador): # Como estamos usando a interface, para a utilização de uma classe(nesse caso uma herança), a gente fala que a classe é uma implementacao da interface
    def trabalhar(self):
        print('O Professor esta trabalhando')

    def ir_para_casa(self):
        print('O Professor esta indo para casa')
    
    def horario_de_almoco(self):
        print('O Professor esta almoçando')

class Engenheiro(Trabalhador):
    def trabalhar(self):
        print('O Engenheiro esta trabalhando')

    def ir_para_casa(self):
        print('O Engenheiro esta indo para casa')
    
    def horario_de_almoco(self):
        print('O Engenheiro esta almoçando')


def comunicar_o_trabalhador(trabalhador: Trabalhador): #Aqui vc coloca o trabalhador interface, para o vs code entender a quem vc esta se referindo
    trabalhador.trabalhar()
    print('Comunicar o trabalhador, para ir para casa')
    trabalhador.ir_para_casa()
    # função que depende de uma classe, que implemente essa interface

p1 = Professor()
p2 = Engenheiro()
comunicar_o_trabalhador(p1) 
comunicar_o_trabalhador(p2)