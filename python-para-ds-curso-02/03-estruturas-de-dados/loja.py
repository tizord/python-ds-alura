# 6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente:
#     Dados do ano 2022
#     Venda maior do que 6000. 
# A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados:
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
# Crie uma lista usando list comprehension para filtrar os valores de 2022 e que sejam maiores que 6000.

vendas_2022 = [vendas[i][1] for i in range(len(vendas)) if vendas[i][0] == "2022" and vendas[i][1] > 6000]
print(vendas_2022)