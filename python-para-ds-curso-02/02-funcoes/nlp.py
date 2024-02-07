# 10) Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP).
# Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e
# filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista.
# Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa
# quantidade de caracteres.
# Use a frase:
#     "Aprender Python aqui na Alura é muito bom"
# para testar o código.

frase = "Aprender Python aqui na Alura é muito bom"
frase = frase.split()
verifica_tamanho = lambda x: True if len(x) >=5 else False
palavras_selecionadas = list(filter(verifica_tamanho, frase))
print(palavras_selecionadas)