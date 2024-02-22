import pandas as pd

dados = pd.read_excel('1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx', sheet_name='GEE Estados')
print(dados)

# Vamos remover alguns dados

dados['Emissão / Remoção / Bunker'].unique() #Para verificar quais são os valores únicos da coluna

# Queremos remover o que é Remoção NCI ou Remoção

(dados['Emissão / Remoção / Bunker'] == 'Remoção NCI') | (dados['Emissão / Remoção / Bunker'] == 'Remoção')
# Acima, temos uma forma de identificar os valores para depois filtrar na base de dados.
# Porém, podemos fazer isso de forma direta, usando o método .isin -> Porque estamos pegando 2 info da mesma col.

dados[dados['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção'])] #Isso é um filtro

# Queremos avaliar, dentro desse filtro, se todos os valores são negativos:
# Para isso, vamos repetir a consulta, adicionando o método loc.
# O método .loc serve para poder selecionar as colunas.

dados.loc[dados['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021]

# Sabendo que os dados de remoção tem que ser < 0, vamos avaliar se todos são menores que 0:

dados.loc[dados['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021].max()

 # Como todos os dados retornaram, como valor máximo, deram 0, logo é correto que todos são remoção ( < 0)

# Agora vamos avaliar se as emissões marítimas e aéreas estão corretas, ou sejam, não pertecem a nenhum estado:

dados.loc[dados['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique()

# O que a consulta acima significa?
# Estamos usando o .loc, que serve para trazer as colunas.
# Depois, nós filtramos o dataset "dados" buscando só os valores da coluna 'Emissao.. que são iguais a 'Bunker'
# E por, fim, nós queremos trazer apenas a coluna 'Estado'.
# Depois, aplicamos o método unique() que retorna apenas os valores únicos.

# Por fim, como avaliamos os pontos que queríamos, vamos filtrar e armazenar o dataset apenas com emissões

dados = dados[dados['Emissão / Remoção / Bunker'] == 'Emissão']

# Agora vamos remover a coluna Emissão / Remoção / Bunker, já que vamos eliminar todos os casos que não são emissão:

emissoes_gases = dados.drop(columns=['Emissão / Remoção / Bunker'])

# Agora veja.
# O método DROP não altera o df original. Ele cria uma cópia. Para alterar o df original temos que usar
# inplace=True.
# Temos o método .pop que elimina uma coluna por vez e sua sintaxe é:
# dataframe.pop(nome_coluna)


##
##
# Vamos fazer agrupamento de dados.

emissoes_gases.loc[:, 'Nível 1 - Setor':'Produto'].columns #Aqui vamos pergar todas as colunas de Nivel 1 até Produto.
colunas_info = list(emissoes_gases.loc[:, 'Nível 1 - Setor':'Produto'].columns)

emissoes_gases.loc[:,1970:2021].columns
colunas_emissao = list(emissoes_gases.loc[:,1970:2021].columns)

# Agora vamos transformar a base de dados usando o método .melt()
# Esse método serve para transformar tabelas com formato wide para long.

emissoes_gases.melt(id_vars=colunas_info, value_vars=colunas_emissao, var_name='Ano', value_name='Emissão')
# Nesse método:
#   id_vars = nome das colunas que desejamos manter,
#   value_vars = colunas que serão transformadas nas colunas principais do format long.
#                uma contendo as categorias com os nomes das colunas e outra contendo os valores
#   var_name = nome da coluna que vai conter o nome das informações,
#   value_name = nome da coluna que vai conter os valores numéricos.

emissoes_por_ano = emissoes_gases.melt(id_vars=colunas_info, value_vars=colunas_emissao, var_name='Ano', value_name='Emissão')

# Foi solicitado a quantidade total de emissão para cada tipo de gás, afim de determinar qual gás é mais emitido.

# Vamos usar o groupby

emissoes_por_ano.groupby('Gás')
emissoes_por_ano.groupby('Gás').groups #Cria um dicionário onde as chaves são os grupos e os valores são os índices das linhas do DF que pertecem a cada grupo.
emissoes_por_ano.groupby('Gás').get_group('CO2 (t)')

# Para que possamos trazer a soma dos grupos, precisamos usar um método agregador em conjunto com o group-by.
# Os métodos agrupadores são:
#   count()
#   sum()
#   mean()
#   median()
#   std()
#   min()
#   max()
#   var()

emissoes_por_ano.groupby('Gás').sum(numeric_only=True) # Aplica esse método apenas nas colunas númericas.
#Poderíamos fazer, também:
emissoes_por_ano.groupby('Gás')[['Emissão']].sum()

emissao_por_gas = emissoes_por_ano.groupby('Gás')[['Emissão']].sum().sort_values('Emissão', ascending=False) # Força ordenar de maneiras decrescente

# Queremos agora, plotar um gráfico para enxergar melhor o resultado

emissao_por_gas.plot(kind='barh', figsize=(10,6))

# Vamos determinar a proporção do CO2 em relação aos demais:

emissao_de_co2 = emissao_por_gas.iloc[0:9].sum()
emissao_total = emissao_por_gas.sum()
porcentual = (emissao_de_co2/emissao_total).iloc[0]


print(f'A emissao de CO2 corresponde a {float(porcentual)*100:.2f}% de emissão total de gases estufa no BR, de 1970 a 2021')
