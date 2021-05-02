#Crie um programa que leia um número inteiro e diga se é par ou impar
from time import sleep
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('ANALISANDO...')
    sleep(2)
    print('O número é par!')
else:
    print('ANALISANDO...')
    sleep(2)
    print('O número é impar')
print('======FIM=====')