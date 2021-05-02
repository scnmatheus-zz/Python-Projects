#Melhore o DESAFIO028 onde o computador vai "pensar" em um número entre 0 a 10
#só que agora o jogador vai tentar advinhar até acertar, mostrando no final, quantos
#palpites foram necessários para vencer.
from random import randint
from time import sleep
computador = randint(0, 10)
numUser = 11
palpites = 0
while computador != numUser:
    numUser = int(input('Digite um número e tente advinhar o que o computador está pensando: '))
    sleep((0.3  ))
    print('PROCESSANDO...')
    sleep(1)
    palpites = palpites + 1
    if numUser < computador:
        print('Mais... tente novamente.')
    elif numUser > computador:
        print('Menos... tente novamente.')
print(f'Parabéns, você venceu! com {palpites} tentativas')