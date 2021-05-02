#Melhore o DESAFIO028 onde o computador vai "pensar" em um número entre 0 a 10
#só que agora o jogador vai tentar advinhar até acertar, mostrando no final, quantos
#palpites foram necessários para vencer.
from random import randint
from time import sleep
n1 = 0
numUser = 1
while n1 != numUser:
    n1 = randint(0, 5)
    numUser = int(input('Advinhe o número que o computador está pensando : '))
    sleep(0.5)
    print('PROCESSANDO...')
    sleep(1)
    if n1 == numUser:
        print('-=-'*8)
        print(f'O computador pensou no número: {n1}')
        print('==========PARABÈNS!! VOCÊ ACERTOU')
        print('-=-'*8)
    elif n1 != numUser:
        print('-=-'*8)
        print(f'O computador pensou no número: {n1}')
        print('===========Você errou, tente novamente!')
        print('-=-'*8)
