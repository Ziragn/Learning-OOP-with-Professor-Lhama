class Pessoa:
    def __init__(self, altura:float, cpf):
        self.altura = altura
        self.__cpf = cpf # Apresentar para os usuários da nossa classe, que a gente não gostaria de utilizar esse atributo, fora da classe.
    
    def apresentar(self):
        print(f'Ola! Minha altura - {self.altura}')
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f'Meu documento - {self.__cpf}')

# OBs: Métodos privados, são aqueles que só podem ser acessados pela própria classe e não pelo objeto. ex: Vou instanciar abaixo um objeto pessoa e vou tentar chamar o método coletar documento direto (vai dar erro, pq ele tá privado com __). A forma de chamar é por meio da própria classe, que é chamando o método apresentar , que chama o método coletar documento
# métodos privados, só podem ser acessados, de dentro da própria classe. > Previne de ficar dando muitas informações, pra quem utilzar a nossa classe.
jorge = Pessoa(1.70, 'asasasa')
jorge.apresentar()