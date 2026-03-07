# O polimorfismo refere-se à capacidade de um mesmo método, ou função, ser aplicado de diferentes maneiras em classes ou objetos distintos.
# 2 métodos com assinaturas iguais, mas com comportamentos diferentes
class ClasseQualquer:
    def fazer(self) -> None: # assinatura
        print('Estou fazendo algo')

class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None: #assinatura
        print('Estou preparando algo')
    
    # def fazer(self) -> None: #assinatura igual a linha 4
    #     print('Estou fazendo outra coisa')

def fazer_func() -> None: # outra forma de polimorfismo
    print('Estou fazendo outra coisa')

obj1 = ClasseQualquer()
obj2 = OutraCoisa()
obj2.fazer = fazer_func # outra forma de polimorfismo, pega da função, em vez de 2 métodos.
obj1.fazer()
obj2.fazer()  # OBserva que no terminal, saiu diferente nos 2, métodos com ass iguais, mas comp diferentes