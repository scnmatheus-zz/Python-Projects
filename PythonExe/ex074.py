#crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla
#depois disso, mostre a listagem dos numeros gerados e indique também o menor
#e o maior valor da tupla
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os números gerados foram {numeros}')
print(f'O menor valor gerado foi {min(numeros)}')
print(f'O maior valor gerado foi {max(numeros)}')