import sqlite3
import os
import pandas as pd


def create_db():
    if os.path.exists('Bd_autos.db'):
        os.remove('Bd_autos.db') # Apaga o banco a cada Lista consultada
    conexao = sqlite3.connect('Bd_autos.db')
    c = conexao.cursor()
    c.execute(''' CREATE TABLE dados(
            Auto text,
            DataInfracao text,
            Enquadramento text,
            Valor text,
            Debito text,
            Vencimento text,
            SituacaoFase text)  
            ''')

# Commit as mudanças:
    conexao.commit()

# Fechar o banco de dados:
    conexao.close()


def cadastrar_demanda_base(auto, data_infra, enquadramento, valor, debito,
                           vencimento, SituacaoFase):
    conexao = sqlite3.connect('Bd_autos.db')
    c = conexao.cursor()

    #Inserir dados na tabela do BD:
    c.execute("INSERT INTO dados VALUES (:Auto,:DataInfracao,:Enquadramento,:Valor,:Debito,:Vencimento,:SituacaoFase)",
              {
                  'Auto': auto,
                  'DataInfracao': data_infra,
                  'Enquadramento': enquadramento,
                  'Valor': valor,
                  'Debito': debito,
                  'Vencimento':vencimento,
                  'SituacaoFase':SituacaoFase

              })
    # Commit as mudanças:
    conexao.commit()
    # Fechar o banco de dados:
    conexao.close()


def consulta_bd():
    conexao = sqlite3.connect('Bd_autos.db')
    c = conexao.cursor()

    #
    c.execute("SELECT *, oid FROM dados")  # Verificar
    dados = c.fetchall()
    consulta = pd.DataFrame(dados, columns=['Auto','DataInfracao','Enquadramento','Valor','Debito',
                                            'Vencimento','SituacaoFase','index'])

    # dados.to_excel(f'''dados_finalizados_{data}.xlsx''',sheet_name='Resultado',index=False)

    # Commit as mudanças:
    conexao.commit()
    # Fechar o banco de dados:
    conexao.close()

    return consulta






auto = 'B123456789'
data_infra = '01/01/1900'
enquadramento = 'tESTE'
valor =  'R$ 90,45'
debito = 'Em Aberto'
vencimento = '01/01/1900'
SituacaoFase = 'Ativo / Publicado Edital NP'


create_db()

cadastrar_demanda_base(auto, data_infra, enquadramento, valor, debito,
                           vencimento, SituacaoFase)

tabela = consulta_bd()
print(tabela.values.tolist())

