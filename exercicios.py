"""1  Faça um Programa que mostre a mensagem "Alo mundo" na tela."""

# print('Alô mundo')

"""2  Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]."""

# num = input('Digite um número: ')
# print(f'O número digitado foi {num}. ')

"""3    Faça um Programa que peça dois números e imprima a soma."""

# num1 = input('Digite um número: ')
# num2 = input('Digite outro número: ')
# num1 = int(num1)
# num2 = int(num2)
# print(num1 + num2)

"""4    Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

# Bim1 = int(input('Digite aqui a nota do 1o bimestre: '))
# Bim2 = int(input('Digite aqui a nota do 2o bimestre: '))
# Bim3 = int(input('Digite aqui a nota do 3o bimestre: '))
# Bim4 = int(input('Digite aqui a nota do 4o bimestre: '))
# média = ((Bim1 + Bim2 + Bim3 + Bim4) / 4)
# print(f'A média é {média}.')
# if média >= 60:
#     print('Este aluno está aprovado. ')
# else:
#     print('Este aluno está REPROVADO. ')

"""5    Faça um Programa que converta metros para centímetros."""

# medid_metros = input('Digite aqui o tamanho em metros: ')
# if not medid_metros. isdigit():
#     print('Por favor, digite um número válido.')
# else:
#     medid_metros = int(medid_metros)
#     medid_cm = medid_metros * 100
#     print(medid_cm)

"""6    Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""

# raio = input('digite aqui o raio do circulo. ')
# if raio. isdigit():
#     raio = int(raio)
#     area = 3.14 * raio ** 2
#     print(area)
# else:
#     print('reveja o valor')
#

"""7    Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário."""


# lado = input('Digite aqui a medida dos lados do seu quadrado: ')
# if lado. isdigit():
#     lado = int(lado)  #  preciso descobrir como fazer o codigo ler num de ponto flutuante.
#     area_quad = lado ** 2
#     print(area_quad)
#
# else:
#     print(f'Reveja o valor de {lado}.' )

"""8    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
"""

# hora_trab = input('Digite aqui seu valor de hora: ')
# hora_mes = input('Digite aqui quantas horas voce trabalhou neste mes: ')

# if hora_trab and hora_mes. isdigit():
#     hora_trab = int(hora_trab)
#     hora_mes = int(hora_mes)
#     total = hora_mes * hora_trab
#     print(total)
# else:
#     print('Reveja os valores informados. ')

# else:
#     print(f'Reveja o valor de {hora_trab}. ')
#
# if hora_mes.isdigit():
#     hora_mes = int(hora_mes)
# else:
#     print(f'Reveja o valor de {hora_mes}. ')
#
# salario_mes = hora_mes * hora_trab
# print(salario_mes)

# CONFERIR ESTE AQUI


"""9    Faça um Programa que peça a temperatura em graus Fahrenheit,
 transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

# F = input('Digite aqui a temperatura em graus Farenheit: ')
# if F .isdigit():
#     F = int(F)
#     Conversao = ((F - 32) / 1.8)
#     print(Conversao)
# else:
#     print('Reveja o valor inserido. ')

"""10   Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

# C = input('Digite aqui a temperatura em graus Celsius: ')
# if C .isdigit():
#     C = int(C)
#     Conversao = ((C * 1.8) + 32)
#     print(Conversao)
# else:
#     print('Reveja o valor inserido. ')

""""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""


"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo."""

# string_1 = 'esta e uma frase.'
# string_2 = 'esta e outra frase.'
# print(string_1)
# print(string_2)
# print(len(string_1))
# print(len(string_2))
# print(len(string_1) == len(string_2))
# print(string_1 == string_2)

"""Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre 
o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o
 usuário pode digitar letras maiúsculas ou minúsculas.
 """

# nome = input('diga seu nome: ')
# nome = nome.upper()
#
# print(nome[::-1]) #  aparentemente esta funcao [:: -1 somente funciona com strings?]

"""Faça um programa que solicite o nome do usuário e imprima-o na vertical."""

# for c in input('diga seu nome. '):
#     print(c)
#
# """Modifique o programa anterior de forma a mostrar o nome em formato de escada."""
#
nome = 'fausto'
# print(nome[:1])
# print(nome[:2])
# print(nome[:3])
# print(nome[:4])
# print(nome[:5])
# print(nome[:6])

# print(f'{nome:.2s}') #  mandando o programa rodar apenas as 2 primeiras strings do nome
#
# numero_de_letras = len(nome)
# if numero_de_letras >= 6 and numero_de_letras <= 10:
#     print('meu nome tem entre 6 e 10 letras.')
# elif numero_de_letras > 10:
#     print('meu nome tem mais de 10 letras. ')
# else:
#     pass
# print(f'A quantidade de letras no meu nome e {len(nome)}.')

""""""
#
# import datetime
#
# currentDateTime = datetime.datetime.now()
# date = currentDateTime.date()
# year = date.strftime("%Y")
# print(f"Current Year -> {year}")

"""Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""

# frase = input('Diga algo: ')
# if len(frase) > 140:
#     print('sua frase excedeu o limite de caracteres, que e de 140. ')
# else:
#     print(f' sua frase tem {len(frase)} caracteres.')

""" Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não."""

