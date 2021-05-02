#DESAFIO 028 ESCREVA UM ALGORITMO PARA UM USÙARIO ADVINHAR O NÙMERO QUE O COMPUTADOR "PENSA"
from random import randint
from time import sleep
n1 = randint(0, 5)
numUser = int(input('Advinhe o número que o computador está pensando : '))
print('PROCESSANDO...')
sleep(2)
if numUser == n1:
    print('Parabéns, você acertou!!!')
else:
    print('Mais sorte na próxima!')

