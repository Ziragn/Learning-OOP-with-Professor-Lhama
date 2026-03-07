from abc import ABC, abstractmethod

class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self):
        pass

    @abstractmethod
    def ir_para_casa(self):
        pass

    @abstractmethod
    def consultar_beneficios(self):
        pass
# L > Uma classe, não deve ser forçada a depender de uma interface que não utiliza.

class Professor(Trabalhador):
    def trabalhar(self):
        print('O Professor esta trabalhando')

    def ir_para_casa(self):
        print('O Professor esta indo para casa')
    
    def consultar_beneficios(self):
        print('Consultando beneficios da CLT')

class ProfessorSubstituto(Trabalhador): #
    def trabalhar(self):
        print('O Professor Substituto esta trabalhando')

    def ir_para_casa(self):
        print('O Professor Substituto esta indo para casa')
   
p2 = ProfessorSubstituto() # Vai dar erro, pq a classe profsubs ñ tem o método consultar beneficios da interface (classe abstrata). #  QUEBRA DA SEGREGRAÇÃO DAS INTERFACES.