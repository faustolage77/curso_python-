"""
1#  faça um programa que peça ao usuário para digitar um número inteiro,
    informe se este número é par ou impar.
    Caso o usuário não digite um número inteiro,informe-o.
"""


# numero_usuario = input('Digite aqui um número inteiro: ')
#
# if not numero_usuario . isdigit():
#     print('Este não é um número inteiro.')
# else:
#     numero_usuario = int(numero_usuario)
#
#     if not numero_usuario % 2 == 0:  #  ficar atento ao indentation e blocos
#         print(f'{numero_usuario} é impar. ')
#     else:
#         print(f'{numero_usuario} é par. ')

"""
2#  faça um programa que pergunte a hora ao usuário, e, baseando-se no horário descrito,
#  exiba a saudação apropriada. exemplo. de 0 as 11 = bom dia. de 12 as 17 = boa tarde
#  de 18 as 23 = boa noite
"""


# hora = input('Quantas horas são? ')


# if hora. isdigit():
#     hora = int(hora)
#     if hora < 0 or hora > 23:
#         print('horário deve estar entre 0 e 23')
#     else:
#         if hora < 11:
#             print('bom dia')
#         elif hora <= 17:
#             print('boa tarde')
#         else:
#             print('boa noite')
# else:
#     print('por favor digite um horário entre 0 e 23. ')


"""
3# Faça um programa que peça o primeiro nome do usuário. se o nome tiver 4 letras ou menos escreva
'seu nome é curto'. se tiver entre 5 e 6 letras, escreva 'seu nome é normal', se tiver mais de 6 letras, escreva 'seu 
nome é muito grande'
"""

nome = input('Qual o seu nome? ')
qtde_de_caracteres = len(nome)

if qtde_de_caracteres <= 4:
    print('seu nome é muito curto. ')

elif qtde_de_caracteres<= 6:
    print('seu nome é normal')

else:
    print('seu nome é grande demais')







