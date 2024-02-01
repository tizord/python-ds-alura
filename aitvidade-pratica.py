import pandas as pd

# 1) Importe o arquivo alunos.csv e armazene seu conteúdo em um DataFrame Pandas.

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

dados = pd.read_csv(url)

print(f'{dados}\n\n')

# 2) Visualize as primeiras 7 linhas do DataFrame e as 5 últimas.

print('Top 7 linhas\n')
top_7 = dados.head(7)
print(top_7)
print(f'{30*'-'}\n\n')

print('Bottom 5 linhas\n')
bottom_5 = dados.tail()
print(bottom_5)
print(f'{30*'-'}\n\n')

# 3) Confira a quantidade de linhas e colunas desse DataFrame.

qtd_l_c = dados.shape
print('Quantidade de dados (L x C)\n')
print(qtd_l_c)
print(f'{30*'-'}\n\n')

# 4) Explore as colunas do DataFrame e analise os tipos dos dados presentes em cada coluna.

print('Informações sobre o DF \n')
print(dados.info())
print(f'{30*'-'}\n\n')


# Extra: Calcule algumas estatísticas descritivas básicas dos dados do DataFrame
# (média, desvio padrão, etc). Dica: pesquise pelo método describe.
print('Estatísticas\n')
print(dados.describe())

# 5) Verifique se a base de dados possui dados nulos e, caso tenha, realize
# o tratamento desses dados nulos da forma que achar mais coerente com a situação.

print(dados.isnull())
qtd_na = dados.isnull().sum()
# Temos 6 notas nulas. Não podemos tirar o aluno da turma e, portanto, vamos atribuir zero.
dados.fillna(0, inplace=True)

# 6) Os alunos "Alice" e "Carlos", não fazem mais parte da turma.
# Sendo assim, remova-os da base de dados.

remover = dados.query('Nome == "Alice" | Nome == "Carlos"').index
dados.drop(remover, inplace=True)

# 7) Aplique um filtro que selecione apenas os alunos que foram aprovados.
filtro_alunos_aprovados = dados['Aprovado'] == True
alunos_aprovados = dados[filtro_alunos_aprovados]

# 8) Salve o DataFrame que possui apenas os alunos aprovados em um arquivo csv chamado
# "alunos_aprovados.csv".

alunos_aprovados.to_csv('alunos_aprovados.csv', index=False, sep=';')

#Extra: Ao conferir as notas dos alunos aprovados, notamos que algumas notas estavam incorretas.
# As alunas que tiraram nota 7.0, na verdade, tinham um ponto extra que não foi contabilizado.
# Sendo assim, substitua as notas 7.0 da base de dados por 8.0. Dica: pesquise pelo método replace

alunos_aprovados.replace(7,8)
alunos_aprovados.to_csv('alunos_aprovados.csv', index=False, sep=';')

# 9) Os alunos participaram de uma atividade extracurricular e ganharam pontos extras.
# Esses pontos extras correspondem a 40% da nota atual de cada um deles. Com base nisso,
# crie uma coluna chamada "Pontos_extras" que contenha os pontos extras de cada aluno
#, ou seja, 40% da nota atual deles.

dados['Pontos_extras'] = dados['Notas']*0.4

# 2) Crie mais uma coluna, chamada "Notas_finais" que possua as notas de cada aluno somada
# com os pontos extras.

dados['Notas_finais'] = dados['Notas'] + dados['Pontos_extras']

# 3) Como houve uma pontuação extra, alguns alunos que não tinham sido aprovados
# antes podem ter sido aprovados agora. Com base nisso, crie uma coluna chamada
# "Aprovado_final" com os seguintes valores:
#   True: caso o aluno esteja aprovado (nota final deve ser maior ou igual a 6);
#   False: caso o aluno esteja reprovado (nota final deve ser menor que 6).

dados['Aprovado_final'] = dados['Notas_finais'].apply(lambda x: True if x >=6 else False)

# 4) Faça uma seleção e verifique quais alunos não tinham sido aprovados anteriormente,
# mas foram aprovados após a soma dos pontos extras.

filtro_aprovacao = (dados['Aprovado'] == False) & (dados['Aprovado_final'] == True)
alunos_aprovados_final = dados[filtro_aprovacao]
alunos_aprovados_final.to_csv('alunos_aprovados_pf.csv', index=False, sep=";")