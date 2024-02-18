import pandas as pd
import requests
import json


# Desafio 1) 
# Faça a leitura do arquivo utilizando a função read_csv da biblioteca Pandas.
# Alguns parâmetros devem ser adicionados
# 1) Verifique se o arquivo CSV está separado por vírgula ou ponto e vírgula.
# 2) A codificação do arquivo é ISO-8859-1.
# 3) As três primeiras linhas linhas do arquivo podem ser desconsideradas, pois o cabeçalho só começa na quarta linha.
# 4) As 9 últimas linhas também podem ser desconsideradas, pois são apenas informações sobre onde os dados foram obtidos.
# 5) Para deletar as últimas linhas é necessário adicionar o parâmetro engine='python'.

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/dados_sus.csv'

dados_sus = pd.read_csv(url, sep=';', encoding='ISO-8859-1', skiprows=3, engine='python', skipfooter=9)
dados_sus.head()
dados_sus.tail()
dados_sus.info()


# Desafio 2)
# Neste desafio, a sua função é efetuar a leitura desse link do Google Planilhas:
# https://docs.google.com/spreadsheets/d/1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw/edit#gid=1214654498
# e depois salvar o DataFrame obtido no formato CSV.

link = 'https://docs.google.com/spreadsheets/d/1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw/edit#gid=1214654498'
id_sheet = '1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw'
url = f'https://docs.google.com/spreadsheets/d/{id_sheet}/gviz/tq?tqx=out:csv&sheet'

dados_co2 = pd.read_csv(url)
print(dados_co2.head())
dados_co2.to_csv('dados_co2.csv', index=False)


# Obtendo dados de uma API

#primeiro vamos trazer os dados com a biblioteca requests:

dados_frutas = requests.get('https://fruityvice.com/api/fruit/all')
resultado = json.loads(dados_frutas.text)
df_frutas = pd.DataFrame(resultado)
print(df_frutas)
# Os dados não estão normalizados

# Desafio 3)
# Normalizar os dados das frutas obtidos pelo JSON.

frutas_normalizado = pd.json_normalize(resultado)
print(frutas_normalizado)

# Desafio 4)
# Lendo uma tabela de uma página web

# Pagina: https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o

# Primeiro vamos ver quantas tabelas temos:
dados = pd.read_html('/home/tizord/Documentos/alura-python/pandas-i-o/Lista-de-países-por-população–Wikipédia-a-enciclopédia-livre.html')
print(dados)
# Sabemos que queremos a tabela 1 (índice 0)
qtd_habitante = dados[0]


# Desafio 5)
# Criar o banco de dados local com a biblioteca SQLAlchemy.
# Escrever os dados do arquivo CSV neste banco de dados local.
# Realizar três atualizações no banco de dados:
#     Atualizar o registro do cliente de ID 6840104 que teve o rendimento anual alterado para 300000.
#     Excluir o registro do cliente de ID 5008809, pois essa pessoa não possui mais conta na instituição financeira.
#     Criar um novo registro de cliente seguindo as especificações abaixo:
#         ID_Cliente: 6850985
#         Idade: 33
#         Grau_escolaridade: Doutorado
#         Estado_civil: Solteiro
#         Tamanho_familia: 1
#         Categoria_de_renda: Empregado
#         Ocupacao: TI
#         Anos_empregado: 2
#         Rendimento_anual: 290000
#         Tem_carro: 0
#         Moradia: Casa/apartamento próprio

url_4 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table ,inspect

# 1 - Criar a engine do BD

engine = create_engine("sqlite:///:memory:")

# 2 - Importando os dados contidos no csv

dados_financeiros = pd.read_csv(url_4)

# 3 - Passando os dados para SQL

dados_financeiros.to_sql('clientes', engine, index=False)

# 4 - Conferindo se os dados estão no BD

inspector = inspect(engine)
print(inspector.get_table_names())

# 5 - Fazendo uma consulta

query_0 = 'SELECT * FROM clientes'

# 6 - Fazendo as consultas propostas:

query_1 = 'UPDATE clientes SET Rendimento_anual=300000 WHERE Id_Cliente ="6840104"'
query_2 = 'DELETE FROM clientes WHERE Id_Cliente="5008809"'
query_3 = 'INSERT INTO clientes (Idade, Grau_escolaridade, Estado_civil, Tamanho_familia, Categoria_de_renda, Ocupacao, Anos_empregado, Rendimento_anual, Tem_carro, Moradia) VALUES (33, "Doutorado", "Solteiro", 1, "Empregado", "TI", 2, 290000, 0, "Casa/apartamento própio")'

with engine.connect() as conn:
    conn.execute(query_1)
    conn.execute(query_2)
    conn.execute(query_3)

# Lendo

print(pd.read_sql_table('clientes', engine))

# Salvando em .csv

dados_financeiros.to_csv('clientes.csv', index=False)