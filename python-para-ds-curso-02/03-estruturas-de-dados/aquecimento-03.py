# 1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

soma = [sum(lista) for lista in lista_de_listas]
print(soma)

# 2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

terceiro_elemento = [lista_de_tuplas[i][2] for i in range(len(lista_de_tuplas))]
print(terceiro_elemento)

# 3. A partir da lista:
lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
# crie um código para gerar uma lista de tuplas em que cada tupla tenha:
    # o primeiro elemento como a posição do nome na lista original
    # o segundo elemento sendo o próprio nome.
lista_tuplas = list(zip(range(len(lista)), lista))
print(lista_tuplas)

# 4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento',
#  a partir da seguinte lista de tuplas:
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

valor_tupla = [aluguel[i][1] for i in range(len(aluguel)) if aluguel[i][0]=="Apartamento"]
print(valor_tupla)

# 5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
# e os valores estão em 
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

mes_despesa = {meses[i]: despesa[i] for i in range(len(meses))}
print(mes_despesa)
