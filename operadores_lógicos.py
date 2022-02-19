"""
Operadores lógicos - aula 4  #  usados para realizar comparaões

and  #  (Verdadeiro e Verdadeiro) = Verdadeiro se todas as operações forem verdadeiras,
ele te retorna True. Basta que 1 seja falsa para que ele te retorne como False
and  #  (Verdadeiro e Falso) = Falso
comparacao1 and comparacao2

or  #  (Verdadeiro OU Verdadeiro) = Para  te retornar True, basta que apenas 1 seja verdadeira
or, not
# not = inversao ou preenchimento de valores vazios
exemplo:

a = 2
b = 3
if not b > a:
    print('B é maior do que a')
else:
    print('A é maior do que b')


in e not in

"""
"""a = ''
b = ''
if not a or b:
    print('Por favor, preencha os valores em branco.')
"""

nome = 'Fausto Lage.'
if 'to' not in nome:
    print('Executei')
else:
    print('Existe o texto')