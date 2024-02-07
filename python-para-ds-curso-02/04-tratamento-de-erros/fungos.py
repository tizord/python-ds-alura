# 7. Você foi contratado(a) como uma pessoa cientista de dados para auxiliar um laboratório que faz
# experimentos sobre o comportamento de uma cultura de fungos. O laboratório precisa avaliar
# constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado 
# recolhidos durante a experimentação para definir a melhor condição para os testes.

# Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das 
# colunas de pressão e temperatura (que vem no formato de listas) e gerar uma nova coluna com o 
# resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao 
# menos 2 tipos de exceções:

# Verificar se as listas têm o mesmo tamanho (ValueError)
# Verificar se existe alguma divisão por zero (ZeroDivisionError)
# Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento,
# com os valores de pressão e temperatura do ambiente controlado.


# Dica: Você pode usar zip() para parear os dados da lista_1 com a lista_2. Crie uma estrutura 
# try-except que caso uma das exceções sejam lançadas, podemos ver o tipo de erro na saída.


## Sem exceção
pressoes1 = [100, 120, 140, 160, 180]
temperaturas1 = [20, 25, 30, 35, 40]

## ZeroDivision Error
pressoes2 = [60, 120, 140, 160, 180]
temperaturas2 = [0, 25, 30, 35, 40]

## ValueError
pressoes3 = [100, 120, 140, 160]
temperaturas3 = [20, 25, 30, 35, 40]

def divide_colunas(pressao: list, temperatura: list) -> list:
    len_pressao = len(pressao)
    len_temperatura = len(temperatura)
    try:
        if len_pressao != len_temperatura:
            raise ValueError("Listas com tamanho diferentes.")
        if 0 in temperatura:
            raise ZeroDivisionError("Temperatura com valor 0 (zero).")
    except Exception as e:
        print(f'{e} - {type(e)}')
    else:
        razao = [round(pressao[i]/temperatura[i], 2) for i in range(len(pressao))]
        resultado = list(zip(pressao, temperatura, razao))
        return resultado

r1 = divide_colunas(pressoes1, temperaturas1)
r2 = divide_colunas(pressoes2, temperaturas2)
r3 = divide_colunas(pressoes3, temperaturas3)