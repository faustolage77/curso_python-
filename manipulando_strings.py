"""Manipulando strings - aula 6
* Strings indices
* Fatiamento de strings [inicio: fim: passo]
* Funcoes built-in len, abs, type, print, etc
 Estas funcoes podem ser usadas diretamente em cada tipo."""


#  positivos        [012345678]
texto =             'python s2'
#  negativos       -[987654321]

# url = 'www.google.com.br/'
# print(url[:-1])

nova_string = texto[2:6]  #  neste caso, o ultimo caracter nao sera impresso, preciso incluir um alem do desejado no
# comando
print(nova_string)
print((texto[:6]))  # se deixar o comando de inicio em branco ele imprimira desde o inicio, presumindo 0
print(texto[7:])
print(texto[-1])  #  neste caso ele pegou o ultimo caracter da string
print(texto[:-2])
print(texto[:6:2])  #  respectivamente  inicio:fim:steps
print(texto[:])  #  aqui ele pega a string inteira
print(len(texto))
#  primeiro caracter = indice 0
#  ultimo caracter = indice -1
