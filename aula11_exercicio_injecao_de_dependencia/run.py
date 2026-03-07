class ConectorBancodeDados: #conector de banco
    def __init__(self) -> None:
        self.connection = None
    
    def conectar_ao_banco(self) -> None:
        self.connection = True
    
class RepositorioDeBanco: #onde faz ações no nosso banco
    def __init__(self, conexao:ConectorBancodeDados) -> None:
        self.__conexao = conexao
    
    def busca_dados(self) -> list:
        if self.__conexao.connection: # se a conexão for True
            return [1,2,3,4,5]
        return None
    
class RegradeNegocio: #uma acao que a gente realiza, pega dados do banco
    def __init__(self, repo:RepositorioDeBanco) -> None:
        self.__repo = repo
    
    def calcular_resultados(self) -> None:
        dados = self.__repo.busca_dados()
        if not dados:
            print('Dados não encontrados, verifique sua conexão com o banco')
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f'O resultado é: {resposta}')

conn = ConectorBancodeDados()
conn.conectar_ao_banco()

repo = RepositorioDeBanco(conn)
regra = RegradeNegocio(repo)
regra.calcular_resultados()


        