# 8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo.
# Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.
# Escreva uma função chamada calcula_pontos que recebe como parâmetros:duas listas de números inteiros, representando:
#     1. Gols marcados 
#     2. Gols sofridos pelo time em cada partida do campeonato.
# A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração:
#     Vitória vale 3 pontos, 
#     O empate vale 1 ponto, 
#     A derrota 0 pontos.

# Para teste, utilize as seguintes listas de gols marcados e sofridos:

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

#"A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"

def calcula_pontos(gp: list, gc: list) -> None:
    pontos = 0
    pontos_maximo = 3 * len(gp)
    for _ in range(len(gp)):
        validador = gp[_] - gc[_]
        if validador > 0:
            pontos += 3
        elif validador == 0:
            pontos += 1
        else:
            pass
    aproveitamento = round((pontos/pontos_maximo), 2)
    aproveitamento = 100*aproveitamento
    resultado = f'A pontuação do time foi de {pontos} e seu aproveitamento foi de {aproveitamento}%'
    print(resultado)

calcula_pontos(gols_marcados, gols_sofridos)