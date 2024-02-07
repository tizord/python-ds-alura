# 6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes,
# você precisa criar uma função que receba uma lista de 4 notas e retorne:
#     Maior nota
#     Menor nota
#     Média
#     Situação (Aprovado(a) ou Reprovado(a))
# Para testar o comportamento da função, os dados podem ser exibidos em um texto:
# "O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"

def analiseDesempenhoAlunos(notas: list) -> None:
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = round(sum(notas)/len(notas), 2)
    if media >= 7:
        situacao = "aprovado"
    else:
        situacao = "reprovado"  
    print(f'O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior_nota} pontos e a menor nota de {menor_nota} pontos e foi {situacao}')

notas_maria = [7.7, 3.5, 6.9, 9.2]

analiseDesempenhoAlunos(notas_maria)