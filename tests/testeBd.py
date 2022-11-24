import sqlite3
import os
from datetime import datetime

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


def clean_bd():
    conexao = sqlite3.connect('Bd_autos.db')
    c = conexao.cursor()

    #
    c.execute("DELETE FROM dados WHERE Auto IS NOT NULL")
    # Commit as mudanças:
    conexao.commit()
    # Fechar o banco de dados:
    conexao.close()


def export_dados():
    conexao = sqlite3.connect(r'Bd_autos.db')
    c = conexao.cursor()
    c.execute("SELECT *, oid FROM dados")  # Verificar
    data = (datetime.today().strftime('%Y-%m-%d %H_%M'))  # data de geração do arquivo
    dados = c.fetchall()
    consulta = pd.DataFrame(dados, columns=['Auto', 'DataInfracao', 'Enquadramento', 'Valor', 'Debito',
                                            'Vencimento', 'SituacaoFase', 'index'])
    consulta.to_csv(fr'''C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\dados_finalizados_{data}.csv''', encoding='utf-8', index=False)
    conexao.commit()
    conexao.close()


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
export_dados()



