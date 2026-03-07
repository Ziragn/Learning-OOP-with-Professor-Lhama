class ConnectionDB:
    def conectar(self):
        print('Conectando ao banco')

class SqlRepository(ConnectionDB):
    def select(self):
        print('Buscando dados no banco SQL')

class NoSQLRepository(ConnectionDB):
    def select(self):
        print('Buscando dados no banco NoSQL')

class DBHandler(): # Se eu coloco NoSQLRepository aqui, quebra o principio de liskov
    def alterTable(self):
        print('Alterando tabela em SQL')

# Sempre que for caminhando para baixo, em uma árvore de heranças, a gente sempre tem q respeitar a idéia da classe pai, ser substituída pela classe filha.

