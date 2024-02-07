# 1. Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a 
# divisão entre esses números.
# O código deve conter um tratamento de erro indicando o tipo de erro que foi gerado caso a 
# divisão não seja possível de realizar.
# Teste o programa com o segundo valor numérico do input igual a 0.
# Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.

print("Esse programa irá calcular a divisão de dois números.")
try:
    n1 = float(input("Insira o primiero número: "))
    n2 = float(input("Insira o segundo número: "))
    divisao = n1 / n2
except Exception as e:
    print(f'Não foi possível realizar a divisão. -- Ocorreu um erro:\n {type(e)} - Erro: {e}')
else:
    print(f'A divisão de {n1} por {n2} é: {divisao}')
finally:
    print("Fim da execução")


# 2. Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser 
# pesquisada no seguinte dicionário:

idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

# armazenando o resultado do valor em uma variável.
# O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado',
# caso ocorra o erro;
# e imprimir o valor caso não ocorra nenhum.
# Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário.

try:
    nome = input("Insira um nome: ")
    resultado = idades[nome]
except KeyError as ke:
    print(f"Nome não encontrado.\nErro:{type(ke)} - {ke}")
else:
    print(f'{nome} :, {resultado}')
finally:
    print("Fim da execução")

# 3. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista
# para float.
# A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista
# caso não tenha ocorrido nenhum erro.
# Por fim, deve ter a cláusula finally para imprimir o texto:
# 'Fim da execução da função'.

lista_1 = [1, 2, 6, 4, 'e']
def converteLista(lista: list) -> list:
    try:
        lista_convertida = [float(i) for i in lista]
    except Exception as e:
        print(f'Tipo do erro: {type(e)}\nErro:{e}')
    else:
        return lista_convertida
    finally:
        print("Fim da execução da função.")

# 4. Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das 
# listas, formando uma lista de tuplas de 3 elementos, no qual:
#   - Primeiro e segundo elemento da tupla são os valores na posição i das listas
#   - Terceiro elemento é a soma dos valores na posição i das listas.
# A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como
# resultado a lista de tuplas. 
# Caso as listas enviadas como parâmetro tenham tamanhos diferentes, a função deve retornar
# um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.'
# Dados para testar a função:
# Valores sem erro:
lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7,9]
# Listas com tamanhos diferentes:
lista3 = [4,6,7,9,10,4]
lista4 = [-4,6,8,7,9]
# Listas com valores incoerentes:
lista5 = [4,6,7,9,'A']
lista6 = [-4,'E',8,7,9]

def agrupaLista(lista1: list, lista2: list) -> list:
    try:
        lista_final = []
        tamanho1 = len(lista1)
        tamanho2 = len(lista2)
        if tamanho1 != tamanho2:
            raise IndexError ("A quantidade de elementos em cada lista é diferente.")
        for i in range(len(lista1)):
            lista_final.append((lista1[i], lista2[i], lista1[i]+lista2[i]))
    except Exception as e:
        print(f'{type(e)} - {e}')
    else:
        return lista_final
    finally:
        print("Fim da execução.")

print(agrupaLista(lista1, lista2))
agrupaLista(lista3, lista4)
agrupaLista(lista5, lista6)    