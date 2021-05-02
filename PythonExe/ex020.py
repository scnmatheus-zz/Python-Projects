from random import shuffle
'''Faça um programa que defina a ordem de apresentação dos alunos'''

nomeum = input('Insira o primeiro aluno: ')
nomedois = input('Insira o segundo aluno: ')
nometres = input('Insira o terceiro aluno: ')
nomequatro = input('Insira o quarto aluno: ')
lista = [nomeum, nomedois, nometres, nomequatro]
shuffle(lista)
print(f'A ordem de apresentação, será:')
print(f'{lista}')