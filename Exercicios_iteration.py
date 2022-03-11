# for f in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:  #  F neste caso é a variavel de contagem
#     invitation = "Hi " + f + ".  Please come to my party on Saturday!"  #  primeiro eu crio a iteracao (acima), depois eu crio as variaveis para trabalhar
#     print(invitation)  #  e entao eu imprimo o comando

#  ao criar loops, criar uma variavel de contagem > criar um parametro (um conjunto, por exemplo) > definir uma variavel que trabalhe com a variavel de contagem


#######

# for convidado in ["Raphael", "Viviane", "Eric", "Dani", "Carol"]:
#     convite = "Olá" + convidado, "seria um prazer te receber na minha festa!"
#     print(convite)  #  aqui neste cofigo "convidado" eh a variavel de contagem > o parametro eh o conjunto de convida

# def someate(limite):
#     soma = 0
#     for numero in range(1, limite+1):
#         soma = soma + numero
#
#     return soma
#
# print(someate(4))
#
# print(someate(1000))

# def someAte(limite):
#     """ Retorna a soma de 1+2+3 ... n """
#
#     soma  = 0
#     numero = 1
#     while numero <= limite:
#         soma = soma + numero
#         numero = numero + 1
#     return soma
#
# print(someAte(4))
#
# print(someAte(1000))
#
# minhaLista = [1,2,3,4,5,6]

# print (minhaLista[0])
# print (minhaLista[1])
# print (minhaLista[2])
# print (minhaLista[2])
# print (minhaLista[4])
# print (minhaLista[5])

#  acima eu iterei de forma MANUAL  a minha lista, abaixo vou fazer isto de forma automatica:

# for valor in minhaLista:
#     print(valor)


#######


# algoritmo para descobrir quantas notas de 1, 10 e 50 preciso para pagar uma conta






nota1 = 1
nota10 = 10
nota50 = 50

valorConta = input("Qual o valor da conta? ")
valorConta = float(valorConta)


while valorConta <= 0:
    print(input("Sua conta deve ter um valor maior que 0: "))

    valorConta = (input("Qual o valor da conta?"))
    valorConta = float(valorConta)


if valorConta > 0 and valorConta < 10:


    notasde1Necessarias = valorConta / 1
    notasde10Necessarias = 1
    notasde50Necessarias = 1
    print(notasde1Necessarias, notasde10Necessarias, notasde50Necessarias)

elif  valorConta > 10 and valorConta < 50:


    notasde1Necessarias = valorConta / 1
    notasde10Necessarias = valorConta / 10
    notasde50Necessarias = 1
    print(notasde1Necessarias, notasde10Necessarias, notasde50Necessarias)

elif valorConta > 50:

    notasde1Necessarias = valorConta / 1
    notasde10Necessarias = valorConta / 10
    notasde50Necessarias = valorConta / 50
    print(notasde1Necessarias, notasde10Necessarias, notasde50Necessarias)


elif valorConta == 1:
    notasde1Necessarias = 1
    print(f"So preciso de uma nota de 1! ")

elif valorConta == 10:
    notasde10Necessarias = 1
    print(f"So preciso de uma nota de 10!  ")

elif valorConta == 50:
    notasde50Necessarias = 1
    print("So preciso de uma nota de 50!")


#  conferir resto de divisao e arredondamento p cima





























