"""while em Python - aula7
utilizado para realizar acoes enquanto uma condicao for verdadeira

requisitos: entender condicoes e operadores
"""

# while True:  #  loop infinito
#     nome = input(' qual o seu nome? ')
#     print(f'ola, {nome}')
#
# print('nao sera executada')

# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         break  #  finaliza o loop
#
#     print(x)
#     x = x + 1
# print('acabou')

# x = 0  #  coluna
#
# while x < 10:
#     y = 0  # linha
#
#     while y < 5:
#         print(f'x vale {x} e y vale {y}')
#         y = y + 1
#
#     x = x + 1
#
#
# #  pensar em circulos ajuda a entender a dinamica

#########CALCULADORA############


while True:

    num_1 = input('digite um numero: ')
    num_2 = input('digite outro numero: ')
    operador = input('digite um operador:')
    sair = input('Deseja sair? [s]sim [n]nao: ')

    if sair == 's':
        break


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('voce precisa digitar um numero. ')


        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)

    elif operador == '-':
        print(num_1 - num_2)

    elif operador == '*':
        print(num_1 * num_2)

    elif operador == '/':
        print(num_1 / num_2)

    else:
        print('digite um valor valido. ')
