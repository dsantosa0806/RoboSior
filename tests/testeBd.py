import os
import sqlite3

def create_db():
    if os.path.exists('Bd_autos.db'):
        os.remove('Bd_autos.db')
    conexao = sqlite3.connect('Bd_autos.db')
    c = conexao.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS dados(
        NUP text,
        CREDOR text,
        COMPLEMENTO text,
        NUMERO1 text,
        DEVEDOR text,
        VENCIMENTO text,
        MORA text,
        SELIC text,
        VALOR text,
        MODALIDADE text,
        NUMERO2 text,
        INFRACAO text,
        NOTIFICACAO text,
        CONSTUICAO text,
        DECURSO text,
        REGIONAL text,
        UNIDADE text,
        ETIQUETA text,
        RESULTADO text)
        ''')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()


create_db()