Nome_de_usuário = input('Digite aqui o seu nome de usuário: ')
Senha = input('Digite aqui a sua senha: ')
Nome_de_usuário_BD = 'lagedamazio'
Senha_BD = '123456'
if Nome_de_usuário == Nome_de_usuário_BD and Senha == Senha_BD:
    print('Você está conectado(a), seja bem vindo(a)!')
else:
    print('Nome de usuário ou senha inválidos')

Saudação = input(f' Olá, {Nome_de_usuário}, você está procurando por mais clientes e por uma forma melhor de organizar seu escritório?')
print(input(f'Ótimo, estamos aqui para ajudar. Diz pra gente, em qual Estado você se localiza?'))


