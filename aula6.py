""" nao iniciar variáveis com numero. utilizar _ para separar """

nome = 'Fausto Lage'
idade = 31  #  int
altura = 1.80  #  float
e_maior = idade > 18  #  bool
peso = 112
imc = peso / altura ** 2 # este operador ** tem precedencia entao nao é necesspario utilizar ()

print('nome:', nome)
print('idade:', idade)
print('altura:', altura)
print('e_maior?:', e_maior)
print('peso:', peso)
print('imc:', imc)


print(nome, 'tem', idade, 'anos', 'de idade', 'e seuu imc é', imc)



