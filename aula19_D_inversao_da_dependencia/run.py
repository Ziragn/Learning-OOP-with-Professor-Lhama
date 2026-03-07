from elementos.interfaces.elemento_interface import ElementoInterface
from elementos.elemento import Elemento
from elementos.elemento2 import Elemento2


class Principal:
    def __init__(self, elem: ElementoInterface) -> None: # precisa de um elemento que venha desta interface, então pode ser qlqr classe que use a interface deste, seja o elemento ou elemento2. Tanto o elemento1, quanto o 2 são úteis aqui na classe principal
        #Obs: Ele ta explicando isso, porque antes a dependência aqui era diretamente de uma classe elemento(), já agora não, pode ser dependente de qlqr classe que venha da interface ElementoInterface.
        #em resumo: Uma classe não depende mais diretamente de outar cclasse física e sim de todo mundo que implementa essa interface  (se torna altamente maleável)
        self.__elem = elem

    def run(self) -> None:
        self.__elem.executar()
        print('Estou finalizando na classe principal')

el = Elemento2()

cl1 = Principal(el)
cl1.run()
