# Quebra do principio aberto/fechado: Nesse exemplo aqui, se eu quiser colcoar um show de magico, vou ter que criar um outro método e outro if

# class Circo:
#     def apresentar(self, command:int) -> None:
#         if command == 1:
#             self.__show_palhaco()
#         if command == 2:
#             self.__show_malabarista()
    
#     def __show_palhaco(self):
#         print('O palhaco esta apresentando seu show')

#     def __show_malabarista(self):
#         print('O malabarista esta apresentando seu show')

# circo = Circo()

# command = 1
# circo.apresentar(command)


class Artista:
    def __init__(self, tipo:str) -> None:
        self.tipo = tipo
    
    def apresentar_show(self) -> None:
        print(f'O {self.tipo} esta apresentando seu show')

class Circo:
    def apresentar(self, artista: Artista) -> None:
        print('O circo esta abrindo')
        artista.apresentar_show()
        print('O publico aplaude')

       


solei = Circo()
magico = Artista('magico')
palhaco = Artista('palhaco')
solei.apresentar(magico)



