"""
operadores relacionais - aula 4

== igualdade
>  maior que
>= maior que ou igual a
<  menor que
<= menor que ou igual a
!= pergunta se é diferente


"""

nome = input('Qual é o seu nome?')
idade = int(input('Qual é a sua idade?'))
idade_menor = 20  #  muito jovem
idade_maior = 30  #  passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo, pois está dentro da idade limite, que é entre {idade_menor} e {idade_maior} anos de idade.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo, pois passou da idade limite, que é {idade_maior} anos de idade.')







