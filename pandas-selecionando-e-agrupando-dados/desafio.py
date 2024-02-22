# 1) Encontre os valores únicos das colunas "Nível 1 - Setor" e "Estado" para identificar
# as atividades econômicas presentes na base de dados e se todos os Estados do Brasil estão presentes no DataFrame.

# 2) Filtre o DataFrame somente com os dados dos Estados da região Sul do Brasil.

# 3) Filtre o DataFrame somente com os dados de "Mudança de Uso da Terra e Floresta" que sejam do Estado do Amazonas.

# 4) Encontre o valor máximo de emissão do ano de 2021 para os dados de "Agropecuária" no Estado do Pará.

import pandas as pd

dados = pd.read_excel('1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx', sheet_name='GEE Estados')

# 0) Primeiro vamos achar as informações gerais sobre o df 'dados'

dados.info()

# 1)

dados['Nível 1 - Setor'].unique()

# (['Processos Industriais', 'Agropecuária', 'Energia', 'Resíduos ','Mudança de Uso da Terra e Floresta'], dtype=object)
dados['Estado'].unique()

# array(['SP', 'BA', 'RJ', 'MG', 'SE', 'PR', nan, 'RO', 'AM', 'PA', 'TO',
#       'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'MT', 'MS', 'GO', 'DF',
#       'ES', 'SC', 'RS', 'AC', 'AP', 'RR', 'BR'], dtype=object)
# Estão todos os Estados.

# 2)

dados_sul = dados.loc[dados['Estado'].isin(['RS', 'SC', 'PR', ])]

# 3) Mudança de Uso da Terra e Floresta" que sejam do Estado do Amazonas

filtro = (dados['Nível 1 - Setor'] == 'Mudança de Uso da Terra e Floresta') & (dados['Estado'] ==  'AM')
dados_am_mut = dados[filtro]

# 4) Máximo de emissão de 2021, "Agropecuária", Pará

max_agropec_pa = dados.loc[(dados['Nível 1 - Setor'] == 'Agropecuária') & (dados['Estado'] == 'PA'), 2021].max()

# Desafio 02 - Agrupamento de Dados

# Para fazer os desafios propostos, vamos aplicar os passos de transformar a tabela de wide para long:

emissoes_gases = dados.drop(columns=['Emissão / Remoção / Bunker'])
colunas_info = list(emissoes_gases.loc[:, 'Nível 1 - Setor':'Produto'].columns)
colunas_emissao = list(emissoes_gases.loc[:,1970:2021].columns)
emissoes_por_ano = emissoes_gases.melt(id_vars=colunas_info, value_vars=colunas_emissao, var_name='Ano', value_name='Emissão')

# 5) Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" para visualizar o dicionário
# contendo as chaves de grupos formados e a lista de índices de cada grupo.

emissoes_por_ano.groupby('Nível 1 - Setor').groups

# 6) Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" e localize os dados do grupo "Agropecuária".

emissoes_por_ano.groupby('Nível 1 - Setor').get_group('Agropecuária')

# 7) Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" para identificar
# a média de emissão de cada atividade econômica no ano de 2021.

media_emissao_2021 = emissoes_por_ano[emissoes_por_ano['Ano']==2021].groupby('Nível 1 - Setor')[['Emissão']].mean()

# 8) Faça um agrupamento de dados com base na coluna "Nível 1 - Setor" para identificar
# a soma de emissão de cada atividade econômica. Ordene os dados da maior para menor emissão.

soma_emissoes = emissoes_por_ano.groupby('Nível 1 - Setor').sum(numeric_only=True).sort_values('Emissão', ascending=False)