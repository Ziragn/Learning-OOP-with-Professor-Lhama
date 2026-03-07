# Aqui eu resolvo o problema do exercício anterior, criando uma outra interface para professorsubstituto.
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

class TrabalhadorTemporario(ABC): 

    @abstractmethod
    def trabalhar(self):
        pass

    @abstractmethod
    def ir_para_casa(self):
        pass


class Professor(Trabalhador):
    def trabalhar(self):
        print('O Professor esta trabalhando')

    def ir_para_casa(self):
        print('O Professor esta indo para casa')
    
    def consultar_beneficios(self):
        print('Consultando beneficios da CLT')

class ProfessorSubstituto(TrabalhadorTemporario): #
    def trabalhar(self):
        print('O Professor Substituto esta trabalhando')

    def ir_para_casa(self):
        print('O Professor Substituto esta indo para casa')
   
p2 = ProfessorSubstituto() 