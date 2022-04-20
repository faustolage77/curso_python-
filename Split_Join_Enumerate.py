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

#
# lista = [  #  criando listas dentro de listas
#     [1,2],
#     [3,4],
#     [5,6]
# ]
#
# for v in lista:
#     print(v[0], v[1])

    # fazer estes exercicios para praticar
    # https: // pynative.com / python - list - exercise -
    # with-solutions /

#### exercicios com listas

# Exercise 1: Reverse a list in Python
# Given:
#
# list1 = [100, 200, 300, 400, 500]
# Expected output:
#
# [500, 400, 300, 200, 100]

# list1 = [100, 200, 300, 400, 500]
#
# print(list1[::-1])

#################


# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item
# from both the list, then the 1st index item, and so on till the last element. any leftover items will
# get added at the end of the new list.

# lista1 = ["Fausto", "Anderson", "Ramon"]
# lista2 = ["Raphael", "Gustavo", "Diogo"]
#
# lista3 = [lista1[0], lista2[0]]
#
# print(lista3)

# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

# numbers = [1, 2, 3, 4, 5, 6, 7]
# resposta = []  #  lista vazia para se tornar o que eu quiser
#
# print(numbers)
#
# for elemento in numbers:  #  iterar sobre meus valores
#     resposta.append(elemento ** 2)
#
#
#
#     print(resposta)


# Exercise 4: Concatenate two lists in the following order

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
# # Expected output:
# #
# # ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
#
# print(list1[0], list2[0], list1[0], list2[1], list1[1], list2[0], list1[1], list2[1])
#
# lista = [
#     ["Maria", "Carlos", "Diego"],     # criando listas dentro de uma lista
#     ["Lucas", "Vitoria", "Miguel"],   #  lembrar da virgula
#     ["PEdro", "Ana", "Valdir"]
# ]
#
#
# for v1 in enumerate(lista, 53):
#     valorEnumerado, minhaLista = v1
#     print(valorEnumerado, minhaLista)
#

#####

#   desempacotamento de listas


lista1 = ["Luiz", "Joao", "Maria" , 1, 2, 3, 5, 6, 7, "Diego", 99, 23]

n1, n2, n3, n4, n5, *outraLista, ultimo_da_lista  = lista1  #  o recurso *outraLista pega "o restante"dos valores nao indicados de forma expressa
#  apos minha funcao * , a variavel definida passa a carregar a info do ultimo elemento da lista
print(lista1)
#  o que nao for definido expressamente em uma variavel propria, será automaticamente armazendado, neste caso
#  pela variavel outraLista

print(ultimo_da_lista)

print(outraLista)














