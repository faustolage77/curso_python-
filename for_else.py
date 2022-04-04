"""for / else em python """

variavel = ["Fausto", "Joaozinho", "Maria"]

comecaComJ = False

for valor in variavel:
    if valor.lower().startswith("j"):
        continue
    print(valor)

else:
    print("Nao existe uma palavra que começa com J ")


