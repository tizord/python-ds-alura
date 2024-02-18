import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data.csv'

dados_mercado = pd.read_csv(url)

# A biblioteca chardet serve para descobrir qual é o encoding de um determinado arquivo.

# import chardet
# with open('/content/dados.csv', 'rb') as file:
#     print(chardet.detect(file.read()))

# Resultado do código acima:
#   {'encoding': 'ISO-8859-1', 'confidence': 0.73, 'language': ''}
# Tendo uma chance de 73% de estar no formato ISO-8859-1, podimos para o pandas abrir com esse encoding:
#
# df = pd.read_csv('/content/dados.csv', encoding='ISO-8859-1')

dados = pd.read_csv(url, nrows=5) # Traz as 5 primeiras linhas.
dados_2 = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income']) # Importa algumas colunas do CSV
# Podemos usar o número das colunas em vez de usar o nome delas. Ficaria:
#   usecols=[0, 1, 4]

#
# IMPORTANDO ARQUIVO FORMATO .XLSX
#
# De posse da URL do arquivo, temos que colocar no final:
# ?raw=True

url_2 = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'
dados_co2 = pd.read_excel(url_2)

# Para saber se o arquivo Excel tem mais de uma planilha:

pd.ExcelFile(url_2).sheet_names # Aqui nós podemos ver todas as planilhas dentro do arquivo Excel.

percapita = pd.read_excel(url_2, sheet_name='emissoes_percapita')
fontes = pd.read_excel(url_2, sheet_name='fontes')

# Podemos escolher quais colunas vamos usar:
intervalo = pd.read_excel(url_2, sheet_name='emissoes_CO2', usecols='A:D')
# Podemos escolher, também, as linhas que vamos usar:
intervalo_2 = pd.read_excel(url_2, sheet_name='emissoes_CO2', usecols='A:D', nrows=10)

# Salvando no Excel

percapita.to_excel('co2_percapita.xlsx', index=False)

'''
Acessando uma planilha do Google Sheets:

1º - Devemos ter o link dessa planilha,
2º - Para trabalhar de forma mais limpa, copiamos o id da planilha em uma variável (sheet_id)
3º - escrever a url usando uma f-string:
    url = f{link/sheet_id}
4º - Após o sheet_id, temos que inserir:
    /gviz/tq?tqx=out:csv&sheet -> Esse parâmetro serve para acessar a API do Google para que seja visualizado os dados.
    o csv no final serve para dizer que queremos os dados em csv
5º - Para acessar uma determinada planilha do arquivo temos que fazer:
    sheet_id = 'link'
    sheet_name = 'nome_da_planilha'
    url_2 = f'link_anterior' e após o "out:csv&sheet" colocamos: "out:csv&sheet={sheet_name}

    ATENÇÃO!!!!

    Muito cuidado com o link!
'''

# LENDO JSON

dados_pacientes = pd.read_json()

# Quando as informações do arquivo JSON não estão 100% corretas (ou seja, tem informações aninhadas)
# Podemos usar o site jsoncrack.com <- para poder ver como está o arquivo JSON.
# Para normalizar, podemos tanto usar simplesmente a função pd.json_normalize('df') mas, as vezes precisaremos
# tomar outra atitude:
#   Ver qual coluna está aninhada e passar ela na função json_normalize, como no exemplo abaixo


dados_pacientes_2 = pd.read_json()

df_normalizado = pd.json_normalize(dados_pacientes_2['Pacientes'])

# Apesar disso, temos que nos atentar para algumas coisas:
#     Podemos usar o parâmetro record_path e passar a coluna, como feito anteriormente. O resultado será o mesmo.
#     Mas em ambos, acabos excluindo as clunas Pesquisa e Ano. Para incluí-las, devemos usar o parâmetro meta:
#     pd.json_normalize(
#     dados_dict, 
#     record_path =['Pacientes'], 
#     meta=['Pesquisa', 'Ano']
#     )
# Por fim, o método json_normalize aplica-se a JSON que contém dados em formato de dicionário ou lista de dicionário.
# Para ler o json em formato json, temos que importar outra biblioteca:
#     import json
# e utilizamos o método json.loads:
#     with open('pacientes_2.json','r') as f:
#         dados = json.loads(f.read())
# Depois podemos fazer:
#     pd.json_normalize(dados, record_path='Pacientes', meta=['Pesquisa', 'Ano'])

## IMPORTANDO HTML

# O Pandas pega os dados que tem tag <table>

# XML

# SQL ALCHEMY
import sqlalchemy

from sqlalchemy import create_engine, MetaData, Table, inspect

# MetaData = Serve para ter as informações do banco de dados,
# Table = Serve para criar/maniuplar dados em uma tabela,
# inspect = serve para inspecionar a estrutura do bd

# Criando o BD

engine = create_engine('sqlite:///:memory:') #Estou usando o BD de maneira local.

url_3 = ''
dados_3 = pd.read_csv(url)
dados_3.head()

# Para passar os dados para SQL temos que usar;

dados_3.to_sql('clientes', engine, index=False) # Colocando os dados em um BD

#Para inspecionar:

inspector = inspect(engine)

print(inspector.get_table_names())

# para fazer consultar temos que fazer as querys:

query = 'SELECT * FROM clientes WHERE Categoria_de_renda="Empregado"'

empregados = pd.read_sql(query, engine)

empregados.to_sql('empregados', con=engine, index=False)

# Para ler a tabela inteira podemos fazer:

pd.read_sql_table('empregados', engine)

# # Ou seja:
# O .read_sql serve para ler uma consulta 
# O .read_sql_table serve para ler uma tabela inteira

# E para escolher as colunas?

pd.read_sql_table('empregados', engine, cols=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual'])

# Quando precisamos atualizar as tabelas do SQL:

query_2 = 'DELETE FROM clientes WHERE ID_Cliente="5008804"'
with engine.connect() as conn:
    conn.execute(query_2)

# No código acima, estamos abrindo uma conexão, para executar a query. E o with garante que vai fechar a conexão após isso.

query_3 = 'UPDATE clientes SET Grau_escolaridade = "Ensino superior" WHERE ID_Cliente="5008808"'
with engine.connect() as conn:
    conn.execute(query_3)

# Para lermos as mudanças:

pd.read_sql_table('clientes',engine)