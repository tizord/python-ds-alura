# 9. Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil.
# Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence:
estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
# A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com:
#     a chave sendo o nome de um Estado
#     valor sendo a contagem de vezes em que o Estado aparece na lista.

dic_estados = {estado: estados.count(estado) for estado in estados}
print(dic_estados)


# 10. Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de pessoas colaboradoras.
# O(A) gestor(a) gostaria de ter um agrupamento da soma dessas pessoas para cada estado. As informações contidas na tabela são
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
# A partir da lista de tuplas, crie um dicionário em que:
#     As chaves são os nomes dos Estados únicos
#     Os valores são as listas com o número de colaboradores(as) referentes ao Estado. 
# Crie também um dicionário em que:
#     As chaves são os nomes dos Estados e
#     Os valores são a soma de colaboradores(as) por Estado.

lista_funcionarios = []

for uf in dic_estados.keys():
    lista_aux = [funcionarios[i][1] for i in range(len(funcionarios)) if funcionarios[i][0] == uf ]
    lista_funcionarios.append((uf, lista_aux))

print('10.a - Estados x Lista de colaboradores do estado')
dic_colaborador_por_estado = {tupla[0]: tupla[1] for tupla in lista_funcionarios}
print(dic_colaborador_por_estado)

print('10.b - Estados x Total de colaboradoes do estado')
dic_funcionarios_agrupados = {chave: sum(valor) for chave, valor in dic_colaborador_por_estado.items()}
print(dic_funcionarios_agrupados)