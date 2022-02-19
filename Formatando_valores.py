"""

Formatando valores - aula 5
:s - Texto (strings)
:d - Inteiros (int)
:f - Numeros de ponto flutuante - (float)
:. - (NUMERO)f - Quantidade de casas decimais que eu quero exibir (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f) #  quero definir que tal string tera uma determinada
quantidade de caracteres, ou um tamanho especifico. exemplo>> quero que meu numero tenha sempre 10 casas, posso
preencher com 0.

> - Esquerda
< - Direita
^ - Centro

"""

# num_1 = 10
# num_2 = 3
# divisao = num_1 / num_2
# #  print('{:.2f}' .format(divisao))
# print(f'{divisao:.2f}')  #  esta forma me parece ser mais facil de utilizar

# nome = 'fausto lage'
# print(f'{nome:.3s}')

# num_1 = 1
# print(f'{num_1:0>10}')  #  neste exemplo=  0>10 = preenchimento, direcao, quantidade de casas
# num_2 = 1150
# print(f'{num_2:0>10}')
# num_3 = 3476
# print(f'{num_3:0>10}')
# num_4 = 553734
# print(f'{num_4:0>10}')
# num_5 = 1990
# print(f'{num_5:0>10}')
# num_6 = 1992
# print(f'{num_6:0>10}')
# num_7 = 1961
# print(f'{num_7:0>10}')
# num_8 = 1993
# print(f'{num_8:0>10}')
# num_9 = 1959
# print(f'{num_9:0>10}')
# num_10 = 1970
# print(f'{num_10:0>10}')
# num_11 = 3456
# print(f'{num_11:0^10}')
# num_12 = 1994
# print(f'{num_12:.2f}')  #  aqui eu converti o numero para float
# print(f'{num_12:0>10.2f}')  #  aqui alem de  converter o numero para float, eu tambem fiz a complementacao de
# # caracteres

# nome = 'fausto lage'
# print((20 - len(nome)) / 2 )
# print(f'{nome:#^20}')

# nome = 'fausto henrique'
# sobrenome = 'lage'
# nome_formatado = '{0:$^20} {1:l>10}'.format(nome, sobrenome)  #  utilizacao de indices = comeca sempre do 0
# print(nome, nome_formatado)

nome = 'Fausto Henrique Lage'
print(nome.lower())  #  tudo minusculo
print(nome.upper())  #  tudo maiusculo
print(nome.title())  #  primeiras letras maiusculas


