import pandas as pd
import matplotlib.pyplot as plt

# Importando os dados

dados = pd.read_csv('aluguel.csv', sep=';') #Pois o separador estava com ";"
print(dados.head(10)) # Por padrão traz as 5 primeiras linhas. Aqui pedimos as 10.
print(dados.tail())
print(type(dados)) # Tipo da variável dados
print(dados.shape) # Formato dos dados
print(dados.columns) # Nome das colunas dos dados
print(dados.info()) # Traz mais informações, mais completo.

#Para trazer os valores de algumas colunas:
dados[['Tipo', 'Quartos', 'Valor']] # Repare nos dois [[]]

# Qual é o valor médio por tipo de imóvel?

media_total = dados['Valor'].mean() # Calcula media total.

# Vamos usar o groupy

media_por_tipo = dados.groupby('Tipo').mean(numeric_only = True)
# Esse método necessita o cálculo após ser invocado.
# O numeric_only = True força o pandas a calcular a média apenas nas colunas numéricas.

media_por_tipo_2 = dados.groupby('Tipo')['Valor'].mean()
# Nesse momento coisas interessantes estão acontecendo.
# Agrupamos por tipo, para podermos calcular a média por tipo.
# Usamos o método mean(). Porém, como especificamos uma coluna ['Valor'], não é mais necessário
# que utilizemos o "numerico_only = True" pois o pandas já vai aplicar o cálculo apenas no campo Valor.

# Agora, vamos ordenar a série por valor.

media_tipo_ordenada = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
# Repare na necessidade de colocar o Valor entre colchetes duplos! Caso contrário irá dar erro.

#Agora vamos plotar:

media_tipo_ordenada.plot(kind='barh', figsize=(14,10), color='purple')

# Precisamos remover os imóveis do tipo comercial

print(dados.Tipo.unique())

imoveis_comerciais = ['Conjunto Comercial/Sala','Prédio Inteiro','Loja/Salão',
                      'Galpão/Depósito/Armazém','Casa Comercial','Terreno Padrão',
                      'Box/Garagem','Loja Shopping/ Ct Comercial','Chácara','Loteamento/Condomínio',
                      'Sítio','Pousada/Chalé','Hotel','Indústria']

imoveis_residenciais = dados.query('@imoveis_comerciais not in Tipo')

qtd_imoveis = imoveis_residenciais.Tipo.value_counts() # Conta quantos imoveis, por tipo.
qtd_imoveis_percentual = imoveis_residenciais.Tipo.value_counts(normalize=True) #Traz o percentual
#Podemos transformar em DF:
qtd_imoveis_percentual = imoveis_residenciais.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')
qtd_imoveis_percentual.plot(kind='bar', figsize=(5,5), color='green', xlabel='Tipos', ylabel='Percentual')
imoveis_residenciais = imoveis_residenciais.query('Tipo == "Apartamento"')
qtd_imoveis_percentual.rename(columns={'Tipo': 'Percentuais'}, inplace=True) #Troca o nome da coluna.

# 5) Calcular a média de quartos por apartamento;

imoveis_residenciais.groupby('Quartos').mean(numeric_only=True)
# R: 2.4816

# 6) Conferir quantos bairros únicos existem na nossa base de dados;
bairros_unicos = len(dados.Bairro.unique()) #Ou dados['Bairro'].unique()
# R: 162 Bairros

# 7) Analisar quais bairros possuem a média de valor de aluguel mais elevadas;
bairros_mais_caros = imoveis_residenciais.groupby('Bairro')[['Valor']].mean().sort_values('Valor', ascending=False)

# 8) Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel mais elevadas.
top_5_bairros = bairros_mais_caros.head()
top_5_bairros.plot(kind='barh', figsize=(5,5), color='red')

## TRATANDO DADOS NULOS

dados.isnull() #Verificando se tem dados nulos,
dados.isnull().sum() #True = 1, False = 0 -> Descobrindo quantidade de dados nulos por coluna
dados.fillna(0) #Trocando os dados nulos por 0
dados = dados.fillna(0)

# Temos outras formas de tratar os dados nulos:
#     df.dropna(): Retira todas as linhas/colunas cuja alguma coluna pelo menos 1 dado nulo,
#     fillna(): Preenche os dados nulos com alguma valor.
#         fillna(method='ffill') -> Preenche os dados nulos com o dado da frente,
#         fillna(methos='bfill') -> Preenche os dados nulos com o dado anterior,
#     interpolate(): Preenche os dados nulos com valores interpolados.

#Agora vamos tirar os dados que possuem ou valor de aluguel 0 ou condominio 0.

dados.query('Valor == 0 | Condominio == 0') # Descobrindo os imóveis,
dados.query('Valor == 0 | Condominio == 0').index #Descobrindo os índices
remover_registros = dados.query('Valor == 0 | Condominio == 0').index
dados.drop(remover_registros, axis=0, inplace=True) #Axis = 0: remove linhas -> Para usar o drop é necessário passar índices
dados = dados.query('@imoveis_comerciais not in Tipo')
dados = dados.query('Tipo == "Apartamento"')
dados.drop('Tipo', axis=1, inplace=True)

# Apartamento que possuem 1 quarto e alguel < 1500

dados['Quartos'] == 1 # Podemos usar isso como o filtro.
filtro1 = dados['Quartos'] == 1
dados[filtro1] # Aqui temos a nossa resposta.

# <1200

filtro2 = dados['Valor'] < 1200
dados[filtro2]

filtro3 = filtro1 & filtro2
apartamentos_filtrados = dados[filtro3]

# Apartamento que possuem pelos menos 2 quartos, aluguel < 3000 e área > 70 m2

filtro4 = (dados['Quartos']>2) & (dados['Valor'] < 3000) & (dados['Area'] > 70)
apartamentos_filtrados2 = dados[filtro4]

dados.to_csv('dados_apartamentos.csv', index=False, sep=";")

# 9) Salvar os df (apartamentos_filtrados e apartamentos_filtrados2) em csv distintos.

apartamentos_filtrados.to_csv('apartamentos_1q_ate_1500.csv', index=False, sep=';')
apartamentos_filtrados2.to_csv('apartamentos_nq_ate_3000_mais_de_70m.csv', index=False, sep=';')

# Criar coluna valor por mes, com os gastos mensais de cada imóvel
# Criar coluna de valor por ano.

# Podemos criar colunas de algumas formas:
# 1) Atribuição direta de valores a uma nova coluna
# df = pd.DataFrame({'A': [1, 2, 3], 'B':[4, 5, 6]})
# df['C'] = [7, 8, 9]

# 2) A partir de operação entre colunas:
# df['D'] = df['A'] + df['B']

# 3) Usando a função assign()
# df = df.assign(E=[10, 11, 12])

# 4) Usando método .apply() para aplciar uma função a uma coluna e criar outra
# df['F'] = df['A'].apply(lambda x: x*2)

dados2 =  pd.read_csv('aluguel.csv', sep=';')
dados2['Valor_por_mes'] = dados2['Valor']+dados2['Condominio']
dados2['Valor_por_ano'] = dados2['Valor_por_mes'] * 12 + dados2['IPTU']

# Criar coluna categórica (com palavras ou texto)
# Col descricao = tipo imovel, bairro, quantaidade quartos e vagas de garagem
# Col possui suite 1/0.

# Para transformar coluna de um tipo para outro -> .astype(tipo)
dados2['Descricao'] = dados2['Tipo'] + ' em ' + dados2['Bairro'] + ' com ' + dados2['Quartos'].astype(str) + \
      ' quarto(s) ' + ' e ' + dados2['Vagas'].astype(str) + ' vaga(s) de garagem'

# Para usar a função EM CADA LINHA nós usamos o .apply(função)
dados2['Possui_suite'] = dados2['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")

dados2.to_csv('dados_para_dev.csv', index=False, sep=';')