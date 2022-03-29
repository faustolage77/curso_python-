##### Tuplas > imutaveis

# tuple_mine = (21, 12, 31)
# print(tuple_mine)
#
# tuple_mine = (31, "Green", 4.7)
# print(tuple_mine)
#
#             #  0   1    2    3    4    5    6  #  index positivo da minha tupla
#             #  -7 -6   -5   -4   -3   -2   -2   #  index negativo da minha tupla
# tuple_mine = ('t','r', 'o', 'g', 'r', 'a', 'm')  #  acessando elementos da tupla
# print(tuple_mine)
#
# print(tuple_mine[1])  #  acessando índices em uma tupla
# print(tuple_mine[3])
#
# print(tuple_mine[-1])  #  -1 acessa o último elemento em uma lista ou tupla, -2 o penultimo, e por ai vai
# print(tuple_mine[-3])

#   slicing ou fatiamento :

#             #  0   1    2    3    4    5    6  #  index positivo da minha tupla
#             # -7  -6   -5   -4   -3   -2   -1   #  index negativo da minha tupla
# tuple_mine = ('t','r', 'o', 'g', 'r', 'a', 'm')

tuple_mine = ('t','r', 'o', 'g', 'r', 'a', 'm')
print(tuple_mine [2:5])  #  estou mandando o programa imprimir do index 2 ao index 5, o que nao inclui o ultimo)

print((7, 45, 13) + (17, 25, 76))  #  concatenando tuplas
print(("Several",) * 4)  #  multiplicando strings

del tuple_mine  #  deletando a minha tupla > se eu printar este codigo terei um erro dizendo que
#  a variavel "tuple_mine" nao está definida

clientes = {"Pedro", "Mariza", "Ana Carolina", "Junior"} #  criando uma lista iteravel

print(tuple(clientes))  #  convertendo minha lista em uma tupla

print(enumerate(clientes))

print(max(clientes))

print(len(clientes))  #  quantidade de elementos da minha tupla
