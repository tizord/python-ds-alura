# 5) Você foi contratado(a) como cientista de dados de uma associação de skate.
# Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas.
# Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.
# Para calcular a pontuação de um(a) skatista, você precisa:
#     Eliminar a maior e a menor pontuação dentre as 5 notas
#     Tirar a média das 3 notas que sobraram.
# Retorne a média para apresentar o texto:

# "Nota da manobra: [media]"
notas = []
qtd_notas = 1
while qtd_notas < 6:
    nota = float(input(f"Insira a {qtd_notas}ª nota: \n"))
    notas.append(nota)
    qtd_notas += 1

def calculaNota(notas: list) -> int:
    notas.remove(max(notas))
    notas.remove(min(notas))
    media = round(sum(notas)/len(notas),2)
    print(f'Nota da manobra: {media}')

calculaNota(notas)