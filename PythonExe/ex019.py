from random import choice
'''o professor quer sortear um dos quatros alunos para apagar o quadro, faça um algortimo
que ajude o professor com seu sorteio.'''
from random import choice
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
lista = [n1, n2, n3, n4]
print(f'O aluno sorteado é: {choice(lista)}')
