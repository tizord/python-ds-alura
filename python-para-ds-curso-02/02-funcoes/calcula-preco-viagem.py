# 9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas:
#     Salvador,
#     Fortaleza,
#     Natal
#     Aracaju.
# O custo da diária do hotel = 150 reais,
# Consumo de gasolina na viagem de carro = 14 km/l,
# Valor da gasolina é de 5 reais o litro. 
# O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.
# Distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, 
# Crie três funções nas quais:
#     1ª função calcule os gastos com hotel (gasto_hotel),
#     2ª função calcule os gastos com a gasolina (gasto_gasolina), 
#     3ª função calcule os gastos com passeio e alimentação (gasto_passeio).

# Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.

# "Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"
CIDADES = ["Salvador", "Fortaleza", "Natal", "Aracaju"]
GASTO_PASSEIO = [200, 400, 250, 300]
DISTANCIAS = [850, 800, 300, 550]

def gasto_hotel(n_dias: int) -> int:
    diaria = 150
    gasto_h = diaria*n_dias
    return gasto_h

def gasto_gasolina(distancia: int) -> float:
    consumo = 14
    preco_gasolina = 5
    quantidade_combustivel = (2*distancia)/consumo
    custo_gasolina = round(preco_gasolina*quantidade_combustivel, 2)
    return custo_gasolina

def gasto_passeio(custo_dia:int, n_dias:int) -> int:
    gasto_p = custo_dia*n_dias
    return gasto_p

cidade = input("Insira a cidade de destino: ")
dias = int(input("Insira a quantidade de dias: "))

numero_cidade_escolhida = CIDADES.index(cidade)
gasto_passeio_cidade_escolhida = GASTO_PASSEIO[numero_cidade_escolhida]
distancia_cidade_escolhida = DISTANCIAS[numero_cidade_escolhida]
gasto_hotel_cidade_escolhida = gasto_hotel(dias)
gasto_gasolina_cidade_escolhida = gasto_gasolina(distancia_cidade_escolhida)
gasto_passeio_cidade_escolhida = gasto_passeio(gasto_passeio_cidade_escolhida, dias)

gasto_total = gasto_hotel_cidade_escolhida + gasto_gasolina_cidade_escolhida + gasto_passeio_cidade_escolhida
gasto_total = round(gasto_total, 2)
print(f'Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {gasto_total} reais')