# 21. Fac¸a um programa que preencha um vetor com os modelos de cinco carros (exemplos de
# modelos: Fusca, Gol, Vectra, etc.). Preencha outro vetor com o consumo desses carros,
# isto e, quantos quil ´ ometros cada um deles faz com um litro de combust ˆ ´ıvel. Calcule e
# mostre:
# (a) O modelo de carro mais economico; ˆ
# (b) Quantos litros de combust´ıvel cada um dos carros cadastrados consomem para
# percorrer uma distancia de 1.000 quil ˆ ometros.


carro1 = input("Me diga qual é seu carro:")  #  definindo os modelos e seu consumo base (fornecidos pelo usuario)
consumo1 = int(input("qual o consumo? "))

carro2 = input("Me diga qual é o carro de comparação:  ")
consumo2 = int(input("qual o consumo? "))

carro1dados = (carro1, consumo1)  #  criando uma tupla para receber os dados dos meus vetores
carro2dados = (carro2, consumo2)

resultado = (carro1dados[1], carro2dados[1])  #  criando outra tupla para armazenar e comparar todas as minhas informacoes


if carro1dados[1] > carro2dados[1]:  #  comparando os valores de consumo utilizando indice das minhas tuplas
    print(f'O carro mais economico é o ', carro1)

else:
    print(f'O carro mais economico é o', carro2)

