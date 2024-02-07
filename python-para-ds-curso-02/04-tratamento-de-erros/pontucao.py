# 5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações
# de estudantes de uma instituição de ensino de acordo com suas respostas num teste.
# Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que
# cada lista possui as respostas de 5 questões objetivas de cada estudante.
# Cada questão vale um ponto e as alternativas possíveis são:
#     A, B, C ou D.
# Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis:
#     Lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida".
#     O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes.
#     Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.

# Os dados para o teste do código são:

# Gabarito da prova:
# gabarito = ['D', 'A', 'B', 'C', 'A']

# Listas teste

# Notas sem exceção:
# testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

# Notas com exceção:
# testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

# Dica: Para verificar se uma entrada da lista não está entre as alternativas possíveis, use a estrutura:
# lista[i] not in ['A','B','C','D']. Por exemplo, 1 not in [2,3,4]... Saída: True.

gabarito = ['D', 'A', 'B', 'C', 'A']
notas_possiveis = ['A', 'B', 'C', 'D']
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def calculaNota(gabarito: list, teste: list) -> list:
    notas_possiveis = ['A', 'B', 'C', 'D']
    nota = 0
    nota_final = []
    try:
        for notas in teste:
            for alternativa in notas:
                validador = alternativa in notas_possiveis
                if validador == False:
                    raise ValueError(f"A alternativa {alternativa} não é uma opção de alternativa válida")
    except ValueError as e:
        print(f'{type(e)}, {e}')
    else:
        for notas in teste:
            for i in range(len(notas)):
                if notas[i] == gabarito[i]:
                    nota += 1
                else:
                    pass
            nota_final.append(nota)
            nota = 0
    return print(nota_final)

__init__ = calculaNota(gabarito, testes_sem_ex)