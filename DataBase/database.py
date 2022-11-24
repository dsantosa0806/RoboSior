import sqlite3
import os
import pandas as pd
from datetime import datetime
from View.alertas import alert

diretorio = r'C:'
past_banco = '\Robot Banco de dados\\'
pasta_relatorios = '\Robot Relatorios\\'


def create_db():
    if os.path.exists(diretorio + past_banco + 'Bd_autos.db'):
        os.remove(diretorio + past_banco + 'Bd_autos.db')  # Apaga o banco a cada Lista consultada
    conexao = sqlite3.connect(diretorio + past_banco + 'Bd_autos.db')
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
    conexao = sqlite3.connect(diretorio + past_banco + 'Bd_autos.db')
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
    conexao = sqlite3.connect(diretorio + past_banco + 'Bd_autos.db')
    c = conexao.cursor()
    c.execute("SELECT *, oid FROM dados")  # Verificar
    dados = c.fetchall()
    consulta = pd.DataFrame(dados, columns=['Auto','DataInfracao','Enquadramento','Valor','Debito',
                                            'Vencimento','SituacaoFase','index'])
    # dados.to_excel(f'''dados_finalizados_{data}.xlsx''',sheet_name='Resultado',index=False)
    conexao.commit()
    conexao.close()

    return consulta


def clean_bd():
    conexao = sqlite3.connect(diretorio + past_banco + 'Bd_autos.db')
    c = conexao.cursor()
    c.execute("DELETE FROM dados WHERE Auto IS NOT NULL")
    conexao.commit()
    conexao.close()


def export_dados():
    conexao = sqlite3.connect(diretorio + past_banco + 'Bd_autos.db')
    c = conexao.cursor()
    c.execute("SELECT *, oid FROM dados")  # Verificar
    data = (datetime.today().strftime('%Y-%m-%d %H_%M'))  # data de geração do arquivo
    dados = c.fetchall()
    consulta = pd.DataFrame(dados, columns=['Auto', 'DataInfracao', 'Enquadramento', 'Valor', 'Debito',
                                            'Vencimento', 'SituacaoFase', 'index'])
    consulta.to_csv(fr'''{diretorio + pasta_relatorios}dados_finalizados_{data}.csv''',
                    encoding='latin1', index=False,sep=';')
    conexao.commit()
    conexao.close()



