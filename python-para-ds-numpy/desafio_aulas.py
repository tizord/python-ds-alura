import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt('citrus.csv', delimiter=',', usecols=np.arange(1,6,1), skiprows=1)

diametro_laranja = dados[:5000,0]
diametro_toranja = dados[5000:,0]
peso_laranja = dados[:5000,1]
peso_toranja = dados[5000:,1]

# plt.plot(diametro_laranja, peso_laranja)
# plt.plot(diametro_toranja, peso_toranja)
# plt.legend(['Laranja', 'Toranja'])

# Implementando reta ax+b para Laranja e Toranja
# Laranja

n = np.size(diametro_laranja)
Xl = diametro_laranja
Yl = peso_laranja

al = (n*np.sum(Xl*Yl)-np.sum(Xl)*np.sum(Yl))/(n*np.sum(Xl**2)-np.sum(Xl)**2)
bl = np.mean(Yl)-al*np.mean(Xl)

reta_laranja = al*Xl + bl
norma_laranja = np.linalg.norm(peso_laranja-reta_laranja)

plt.plot(diametro_laranja, peso_laranja)
plt.plot(Xl,reta_laranja)

# Toranja

n = np.size(diametro_toranja)
Xt = diametro_toranja
Yt = peso_toranja

at = (n*np.sum(Xt*Yt)-np.sum(Xt)*np.sum(Yt))/(n*np.sum(Xt**2)-np.sum(Xt)**2)
bt = np.mean(Yt)-at*np.mean(Xt)

reta_toranja = at*Xt + bt

plt.plot(diametro_toranja, peso_toranja)
plt.plot(Xt,reta_toranja)

norma_toranja = np.linalg.norm(peso_toranja-reta_toranja)

# Testando múltiplos coeficientes

# Primeiro é necessário criar uma lista com possíveis coeficientes angulares:
alfas = np.random.uniform(low=1, high=25, size = 100)

# Depois criamos uma array que vai armazenar as normas:
normas_laranja = np.array([])
normas_toranja = np.array([])

# Fazemos um for para calcular Y = ax+b para cada a e calculamos a norma:
for i in range(100):
    normas_laranja = np.append(normas_laranja, np.linalg.norm(peso_laranja - (alfas[i]*Xl+bl)))
    normas_toranja = np.append(normas_toranja, np.linalg.norm(peso_toranja - (alfas[i]*Xt+bt)))

print(normas_laranja)

# Agrupando os dados:

dados_agrupados = np.column_stack([alfas,normas_laranja, normas_toranja])
print(dados_agrupados.shape)

# Para salvar o arquivo:

np.savetxt('dados_citrus.csv', dados_agrupados, delimiter=',')

print("Fim")

