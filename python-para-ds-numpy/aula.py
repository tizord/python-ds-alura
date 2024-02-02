import numpy as np

#np.loadtxt('apples_ts.csv', delimiter=',')

# Arrays em numpy só conseguem ter informações de 1 tipo por array.

dados = np.loadtxt('apples_ts.csv', delimiter=',', usecols=np.arange(1, 88, 1))

# Repare que o np.arange(x, y, z): Cria um array de range:
#     iniciando em x (inclusivo),
#     terminando em y (exclusivo, ou seja y-1),
#     com passo de z.
# Nesse caso: começa em 1, vai até 87, de 1 em 1 ([1, 2, 3, ..., 86, 87])

dados.size #Traz o tamanho da array,
dados.shape #Traz o formato da array,
dados_transpostos = dados.T #Transpõe a array.
datas = dados_transpostos[:,0]
precos = dados_transpostos[:,1:6]

import matplotlib.pyplot as plt

# plt.plot(datas, precos[:,0])


datas = np.arange(1, 88, 1)
Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

## Olhando apenas Moscow

Moscow_ano1 = Moscow[0:12]
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

plt.plot(np.arange(1,13,1), Moscow_ano1)
plt.plot(np.arange(1,13,1), Moscow_ano2)
plt.plot(np.arange(1,13,1), Moscow_ano3)
plt.plot(np.arange(1,13,1), Moscow_ano4)
plt.legend(['Ano1', 'Ano2', 'Ano3', 'Ano4'])
parada = []

np.array_equal(Moscow_ano1, Moscow_ano2) #Mede se as duas arrays são iguais.
np.allclose(Moscow_ano3,Moscow_ano4, 15) #Mede se a distancia entre ano3 e ano4 é até 15

plt.plot(datas, Kaliningrad)
np.isnan() #Indica quais valores são nan (TRUE/FALSE)
# Pode-se usar a seguinte estrutura: sum(np.isnan(array)) pois, cada valor nan retorna 1 True (1).
# A soma será n*True (n*1)

#Uma forma de tratar valores NaN é calcular a média dos valores i-1 e i+1

