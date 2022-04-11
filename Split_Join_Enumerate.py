"""Split, Join, Enumerate em Python
Split - dividir uma string
Join - juntar uma lista
Enumerate - Enumerar elementos da lista ( apenas objetos iteraveis
"""

# string = "O Brasil é o país do futebol, o Brasil é penta."
# lista_1 = string.split(' ')
# lista_2 = string.split(',')


# for valor in lista_2:
#     print(valor.strip())  #  a funcao .strip() remove os espaços do inicio e do fim da minha string

# print(lista_1)
# print(lista_2)
#
# for palavra in lista_1:
#     print(f"a palavra {palavra} apareceu {lista_1.count(palavra)}x na frase")

#
# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x) ')


#########
string = 'O Brasil é penta.'
lista = string.split(' ')

# string2 = ','.join(lista)  #  juntar elementos de uma listga com join
#
# print(string)
# print(lista)
# print(string2)

#########

# for indice, valor, in enumerate(lista):  #  descobrindo a qual indice corresponde cada um dos valores do meu argumento
#     print(indice, valor, lista)


lista = [  #  criando listas dentro de listas
    [1,2],
    [3,4],
    [5,6]
]

for v in lista:
    print(v[0], v[1])