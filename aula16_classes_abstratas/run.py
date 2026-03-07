from abc import ABC, abstractmethod
 #biblioteca abc são os elementos abstratos que temos em python, esse ABC é uma classe, criadora de classes abstratas

class Pessoa(ABC): #Ao fazer isso, a classe pessoa, se torna uma classe abstrata. 
    # Classe abstrata, não possui objetos - só pode ser mãe (utilizando herança)
    def correr(self):
        print('A pessoa esta correndo de manhã')

    @abstractmethod # minha classe filha, deve criar um método 'trabalhar'
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print('O Professor esta dando aula')

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print('O Cozinheiro esta cozinhando')

# p1 = Pessoa() #Daria erro
# p1.correr()

p1 = Professor()
p1.trabalhar()
p1.correr()
# a classe abstrata geralmente é uma classe mais genérica, abrangente, e tem as especificações nos métodos abstratos
# Todos aqueles que utilizam herança da classe abstrata, vão ter de implementer OBRIGATORIAMENTE, o método abstrato.