# principio da injeção de dependencia.
# No exercicio da associação de classes (pessoa / interruptor), a classe pessoa não está 100% dependente da classe interruptor, pois vc consgue instanciar ela sozinha e ainda consegue chamar o método dormir, sem haver um objeto da classe interruptor.

class Celular:
    def __init__(self, modelo:str) -> None:
        self.modelo = modelo
    
    def enviar_mensagem(self, mensagem:str):
        print(f'Enviando a mensagem: {mensagem}')
    
    def abrir_emails(self):
        print(f'Abrindo emails')
    
    def abrir_youtube(self):
        print(f'Abrindo o youtube')

class Pessoa:
    def __init__(self, celular:Celular): #Aqui tem uma relação de dependencia, pq entra diretamente no atributo, a classe pessoa precisa da definição de um objeto da classe celular
        self.__celular = celular #dependencias devem ser tratadas como codigos privados

    def pedir_pizza(self):
        print('Buscando o celular')
        print('definindo o sabor')
        self.__celular.enviar_mensagem('quero uma de calabresa')
    
    def estudar(self):
        print('Sentando no computador')
        self.__celular.abrir_youtube()

iphone = Celular('iphone')
umberto = Pessoa(iphone)
umberto.pedir_pizza()
umberto.estudar()


        