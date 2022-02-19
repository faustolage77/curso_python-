usuário = input('Qual o seu usuário?')
senha = input('Qual é a sua senha?')
usuário_banco_de_dados = 'fausto'
senha_banco_de_dados = '123456'

if usuário == usuário_banco_de_dados and senha_banco_de_dados == senha:
    print('Você esta conectado no sistema')
else:
    print('Usuário ou senha inválidos')
