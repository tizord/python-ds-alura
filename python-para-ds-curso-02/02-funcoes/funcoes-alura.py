#Exercícios propostos

# 1) Escreva um código que lê a lista abaixo e faça:
# 1.1) A leitura do tamanho da lista,
# 1.2) A leitura do maior e do menor valor,
# 1.3) A soma dos valores da lista

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

tamanho_lista = len(lista)
maior_lista = max(lista)
menor_lista = min(lista)
soma_lista = sum(lista)

print(f'A lista possui {tamanho_lista} números em que o maior número é {maior_lista} e o menor número é {menor_lista}. \nA soma dos valores presentes nela é igual a {soma_lista}')

# 2) Escreva uma função que gere a tabuada de um número, de acordo com a escolha do usuário.

numero = int(input("Insira um número: "))
multiplicar = list(range(1,11))
tabuada = list(map(lambda x: numero*x, multiplicar))
print(f'A tabuada do {numero} é: \n{tabuada}')

# 3) Crie a função que leia a lista abaixo e retorne uma nov alista com os múltiplos de 3
lista_2 = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplos_3(lista: list) -> list:
    lista_de_multiplos = []
    for numero in lista:
        if numero % 3 == 0:
            lista_de_multiplos.append(numero)
        else:
            pass
    return lista_de_multiplos

print(multiplos_3(lista_2))

# 4) Crie uma lista dos quadrados dos números da seguinte lista:
lista_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_quadrados = list(map(lambda x: x**2, lista_3))
print(lista_quadrados)