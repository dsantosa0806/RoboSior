import pandas as pd


array = ['B123456789','B987654321','B 12345671']


df = pd.DataFrame(data=array,columns=['auto'])
df['Teste']= 'teste'
df['Teste2'] = 'teste2'
print(df)

# verificação de quantas colunas existem no Df
# for col in df.columns:
    # print(col)

# percorrendo o array de autos
for i, auto in enumerate(df['auto']):
    # print(auto)
    if len(auto) < 10 or len(auto) > 10:
        # print(f'verificar o tamanho do auto - {auto}')
        break
    elif ' ' in auto:
        # print(f'o auto - {auto}, contém espaço(s) em branco')
        break
    elif '\t' in auto:
        # print(f'verifique o auto - {auto}')
        break


