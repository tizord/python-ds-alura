# 6. Você está trabalhando com processamento de linguagem natural (NLP). 
# Sua líder requisitou que você criasse um trecho de código que recebe uma lista com as palavras 
# separadas de uma frase gerada pelo ChatGPT.
# Você precisa criar uma função que avalia cada palavra desse texto e verificar se o tratamento para
# retirar os símbolos de pontuação:
# (',' '.', '!' e '?') foi realizado.
# Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em que foi detectado
# o uso de uma pontuação por meio da frase:
# "O texto apresenta pontuações na palavra "[palavra]"."
# Essa demanda é voltada para a análise do padrão de frases geradas pela inteligência artificial.

# Dica: Para verificar se uma ou mais das pontuações estão presentes em cada palavra,
# utilize a palavra chave or na condição if. Por exemplo, 'a' in 'alura' or 'b' in 'alura'… Saída: True



lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

def detectaPontuacao(lista: list) -> str:
    lista_pontuacao = [',', '.', ';', '!', '?']
    try:
        for palavra in lista:
            for pontuacao in lista_pontuacao:
                verificador = pontuacao in palavra
                if verificador == True:
                    raise ValueError(f'O texto aprensetna pontuações na palavra: {palavra}')
    except ValueError as e:
        print(f'{type(e)}\n\n{e}')
    else:
        print("O tratamento foi feito.")

__init__ = detectaPontuacao(lista_nao_tratada)