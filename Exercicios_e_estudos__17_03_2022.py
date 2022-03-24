# notas = [10, 9 , 8 , 7, 8.88, 7.32 ]
#
# print(max(notas))  #  max retorna o maior valor em um conjunto de valores
#
# print(min(notas))  #  min retorna o menor valor em um conjunto
#
# n = 9

"""if n % 2 == 0:  #  esta operaçao checa se o resto da divisao de um numero por 2 ( ou seja se ele eh par ou impar) eh igual a 0 
    print(" it is an even number ")

else:
    print("it is an odd number ")


"""
# mochila = "mochila"
# letra = mochila[4]  #  extraindo uma letra especifica da minha string
# print(letra)
#
# segmento = mochila[0:3]  #  aqui o programa extrai um substrato , um segmento da minha string. [0:3] quer dizer que ele irá pegar o character comecando do indice 0 ate o indice 3, mas sem inclui-lo
# print(segmento)
#
# segmento2 = mochila[-1:]
# print(segmento2)

##############


""" nota = 76
minimo = 50

if nota >= minimo:
    print("aprovado ")

else:
    print("reprovado")
"""
#
# numero = 78
# if numero % 2 == 0:
#     print("é par ")
#
# else:
#     print("é impar ")

# idade = input("Qual a sua idade? ")  # definicao das variaveis que irao controlar o fluxo do programa
# idade = int(idade)
# maioridade = 18
#
# if idade >= maioridade:  #  utilizacao do perador para determinar o output
#     print("maior de idade ")
#
# else:
#     print("menor de idade")


# numero1 = 8
# numero2 = 13
# soma = numero1 + numero2
#
# if soma < 10:
#     print(f"a soma é {soma}. ")
#
# else:
#
#     print("a soma é maior que 10.")


# num = 83
# if 83 % 2 != 0:  #  estou checando se o resto da divisao do numero por 2 eh igual a 0, ou seja, se o numero eh impar ou par.
#     print(" o numero é impar")
# else:
#     print("o numero é par ")


# def find_max(nums):
# max_num = float("-inf") # smaller than all other numbers
# for num in nums:
# if num > max_num:
# # (Fill in the missing line here)
# return max_num

###################


# numeros = [12, 3, 18, 10, 7, 2, 3, 6, 1]  #  nome de variavel guardando a minha lista
# soma = 0  #  importante definir a variavel soma antes de começar o loop
#
# for x in numeros:  #  iterar a lista
#     soma = soma + x   #  ele vai somar a variavel soma, que inicialmente tem o valor de 0 todos os valores da lista, me dizendo quanto valem todos os items da lista somados
#     print(f"a soma é: {soma}")

######################################

# crie um programa que use um loop for para somar as listas
#
# marks = [3, 8, 19, 6, 18, 29, 15]  #  definindo as listas
# idades = [12, 17, 14, 18, 11, 19, 16]
# mileage = [15, 67, 89, 123, 76, 83]
# cups = [7, 10, 3, 5, 8, 16, 13]
#
# somaMarks = 0 #  definir meus contadores
# somaIdades = 0
# somaMileage = 0
# somaCups = 0
#
# for x in marks:  #  iterar sobre os valores constantes das minhas listas
#     somaMarks = somaMarks + x
#     print(somaMarks)
#
# print("######")
#
# for y in idades:
#     somaIdades = somaIdades + y
#     print(somaIdades)
#
# print("######")
#
# for z in mileage:
#     somaMileage = somaMileage + z
#     print(somaMileage)
#
# print("######")
#
# for k in cups:
#     somaCups = somaCups + k
#     print(somaCups)
#
# print("######")  #  apenas para separar um resultado do outro e tornar o codigo mais legivel
#
# total = somaMileage + somaCups + somaIdades + somaMileage  # somando todos os resultados para obter meu total
# print(total)
#



########################

#  create a program do iterate through the following list and include the message "I listen to (each of the music genre)
#  use the for loop, len() abd range().

# folders = ["Rumba", "House", "Rock"]
#
# for genre in folders:
#     print(f'I listen to {genre} ')


#####################

# marks = [1, 12, 5, 18]
#
# for i in marks:
#     print(i)
#
# else:
#     print("No more items.")  #  utilizando else em um for loop

#####################


# i = 0
# while i < 6:  #  definindo os parametros do meu loop while
#     if i == 5:
#         break  #  aqui ele para o loop pois a minha variavel se tornou igual a 5
#
#     print(i)
#     i = i + 1
# else:
#     print("inside else ")

########################

#  > Write a program that utilizes the while flow control statement to display the sum of all odd numbers from 1 to 10

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #  determinei meu range, que é de 1 a 10
#
# soma = 0  #  criando uma variavel vazia > contador> para acumular meus valores
#
# for numero in numbers:  #  determinando que o programa leia todos os numeros naquele conjunto
#
#     while numero % 2 != 0:  #  aqui eu descubro se o numero eh impar ou par
#
#         soma = numero + soma  #  apos descobrir se meu numero eh par ou impar, se for impar eu o somo a minha soma, que
#         #  é 0, acumulando o valor do meu numero
#
#         print(soma)
#
#         break #  fazer com que meu loop se encerre após encontrar a minha soma




####################
# break and continue statement


#
# track = 0
# while track < 4:
#
#     print("Within the loop ")
#
#     track = track + 1
#     print("Now within the segment ")


# for tracker in "bring":  #  iterando sobre a string definida
#     if tracker == "i":  #  determinando o meu range, qual sera meu criterio para parar
#
#         break  #  determinando que o programa pare de rodar ao encotnrar determinado parametro
#     print(tracker)  #  mandando imprimir meu resultado, apos analisar todo o meu codigo
# print("The end ")

# for tracker in "bring":
#     if tracker == "i":  #  definindo qual elemento nao será lido pelo codigo
#         continue  #  determinando que o programa salte meu rastreador, nao lendo, e lendo apenas o restante da minha string definida la em cima
#     print(tracker)
# print("finished")

#  exemplo: data recovery software

#############

#  Listas

# family = ["Smith", "Mary", "Alicia", "Elijah"]  #  using brackets [] we stored data to a variable "family"

#  through listing we can store as many values within a variable as we like.

# print(family)
# print(family[0])  #  utilizando o comando para buscar um indice (index) especifico dentro da minha lista
# print(len(family))  #  a funcao len() aqui me mostra o comprimento, ou seja, a quantidade de itens da minha lista
# print(family[-1])  #  o comando -1 me mostra o ultimo item da lista

# numbers = [312, 1434, 68764, 4627, 84, 470, 9047, 98463, 389, 2]
# high = numbers[0]  #  criando uma variavel com o valor do 1o numero da lista
# for x in numbers:  #  iterando minha lista para avaliar os valores
#     if x > high:
#         high = x  #  aqui a logica do algoritmo faz  o seguinte: se , ao iterar sobre os valores da lista,
#         #  o programa descobre que o meu x é maior que o meu high (0) o meu high se torna igual a x, sempre
#         #  ficando atualizando e me mostrando o maior valor naquele momento da iteraçao
#         print(f'The highest number is {high}')

# listas 2d

# matrix = [
#     [19, 11, 91],  #  separar por virgulas
#     [41, 25, 54],
#     [86, 28, 21]]
#
# print(matrix)
# print(matrix[0][0])   #  aqui utilizei o primeiro [0] para determinar que o programa busque a 1a lista
# #  e o primeiro [0] para determinar que o programa busque o 1o item desta lista
# print(matrix[1][1])
# print(matrix[2][2])  #  lembrando que a contagem de indices, seja para acessar a lista ou um elemento começa do "0"
# print(matrix[2][0])



#   metodos de lista
#
# numbers = [11,22,33,44,55,66,77,13,77]
#
# numbers.append(10)
# numbers.append(77)  #  adiciono um numero ou valor ao fim da lista
# numbers.insert(2, 20)  #  inserir um numero ou valor no meio da lista
# numbers.remove(77)  #  removo um numero da minha lista mas somente sera removido na primeira aparica. se o
# # numero se repetir de novo la na frente ele nao sera removido
# # numbers.clear()  #  apago o conteudo da minha lista
# numbers.index(44)
#
# print(numbers)
# print(numbers.index(44))  #  aqui estou pedindo ao programa para me informar o indice de um determinado valor da mina
# # lista
#
# print(43 in numbers)  #  utilizado para descobrir se um elemento existe em uma lista > aqui ele está perguntando
# print(numbers.count(77))  #  pergunto quantas vezes determinado valor aparece na minha lista


##########
# Tuplas
#
# numbers = (19,21,28,10,11)  #  tuplas sao imutaveis
# # numbers[0] = 10
# # print(numbers)  #  nao consigo realizar a operacao pois nao posso mudar o valor do indice 0 na tupla
#
# numbers = (1,2,3,4,5)  #  posso dar um overwrite e mudar a tupla, escrevendo-a novamente do 0
# print(numbers)
#

# ages = (25, 30, 35, 40)  #  criando uma tupla com valores de idade
# Drake = ages[0]  #  atribuindo uma idade a cada um com meu indexador []
# Emma = ages[1]
# Sully = ages[2]
#
# # print(ages)
# #
# # print((Drake, Emma, Sully))
#
# Drake, Emma, Sully, Sam  = ages

########

# Dictionaries > estrutura de dados que nos permite memorizar a informacao
# em um formato de par caracter - valor  {}

# alumniAge = {'Andrea': 23, 'John': 28}
# print(alumniAge)
#
usuario1 = {'nome': 'Sam', 'age': 40, 'phone': 123456789, 'married': False}

print(usuario1)

print(usuario1['nome'])
print(usuario1['married']) #  aqui estou utilizando uma operacao semelhante a de indices
#  para pesquisar informacoes especificas de um usuario contidas em uma tupla
#  aqui eu nao conseguiria, por exemplo, pedir print(usuario1[0]), o programa
# me daria um erro . preciso saber exatamento o nome ou o valor da informacao que estou tentando acessar

usuario1['phone'] = 345567890    #  posso "editar" e atualizar informacoes nos meus dicionarios, como fiz aqui
#  digamos que em um banco de dados ha um telefone incorreto de um cliente, por exemplo, assim consigo consertar


print(usuario1['phone'])

usuario1['profession'] = 'programmer'  #  adicionando uma nova variavel , ou seja, informacao nova para meu dicionario

print(usuario1['profession'])

print(usuario1.get('kids', 'invalid'))  #  esta função get serve para impedir que o programa te retorne um erro caso vc ou o usuario
#  insira um termo errado ao tentar acessar o dicionario (ficar atento pois nao entendi mt bem como funciona)

# usuario1.clear()  #  aqui estou limpando os dados do meu dicionario
# print(usuario1)

usuario1.copy()
print(usuario1)  #  me retorna uma copia do meu dicionario

# usuario1.fromkeys(seq[,v]):  #  nao entendi
# print(usuario1)