import sqlite3
import os
import pandas as pd


def create_db():
    bd = 'Bd_autos.db'
    if not os.path.exists(bd):
        conexao = sqlite3.connect(bd)
        c = conexao.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS dados
        (
        Auto text,
        Data Infracao text,
        Enquadramento text,
        Valor text,
        Debito text,
        Vencimento text,
        Situacao_Fase text,
        )    
        ''')

        # Commit as mudanças:
        conexao.commit()

        # Fechar o banco de dados:
        conexao.close()


def cadastrar_demanda_base(auto, data_infra, enquadramento, valor, debito,
                           vencimento, situacao_fase):
    conexao = sqlite3.connect('Bd_autos.db')
    c = conexao.cursor()

    #Inserir dados na tabela do BD:
    c.execute("INSERT INTO dados VALUES (:Auto,:Data Infracao,:Enquadramento,"
              ":Valor,:Debito,:Vencimento,:Situacao_Fase)",
              {
                  'Auto': auto,
                  'Data Infracao': data_infra,
                  'Enquadramento': enquadramento,
                  'Valor': valor,
                  'Debito': debito,
                  'Vencimento':vencimento,
                  'Situacao_Fase':situacao_fase

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
    consulta = pd.DataFrame(dados, columns=['Auto','Data Infracao','Enquadramento','Valor','Debito',
                                            'Vencimento','Situacao_Fase'])

    # dados.to_excel(f'''dados_finalizados_{data}.xlsx''',sheet_name='Resultado',index=False)

    # Commit as mudanças:
    conexao.commit()
    # Fechar o banco de dados:
    conexao.close()

    return consulta
