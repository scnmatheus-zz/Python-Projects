#refaça o desafio 009, mostrando a tabuada de um número que o usuario escolher,
#usando laço de repetição

calc = int(input('Digite um número inteiro: '))
for c in range (0, 11):
    tabuada = calc*c
    print(f'A tabuada de {calc} é {calc}X{c} = {tabuada}')
