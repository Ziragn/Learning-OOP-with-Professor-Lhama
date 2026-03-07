class Interruptor:
    def __init__(self, comodo:str) -> None:
        self.comodo = comodo
    
    def acender(self) -> None:
        print(f'Acendeu as luzes do {self.comodo}')   
    
    def apagar(self) -> None:
        print(f'Apagou as luzes do {self.comodo}')

class Pessoa:
    def acender_luzes(self, interruptor:Interruptor) -> None: #Só consigo ver os metodos da classe acima, por causa da tipagem
        interruptor.acender()

    def apagar_luzes(self, interruptor:Interruptor) -> None:
        interruptor.apagar()
    
    def dormir(self) -> None:
        print('A pessoa foi dormir')

Agnaldo = Pessoa()
interruptor_sala = Interruptor('sala')
interruptor_quarto = Interruptor('quarto')
Agnaldo.acender_luzes(interruptor_sala)
Agnaldo.apagar_luzes(interruptor_quarto)

# AQUI É UMA ASSOCIAÇÃO, ONDE UMA CLASSE UTILIZA FUNCIONALIDADES DE OUTRA CLASSE.


