#faça um programa que jogue par ou impar, só irá interrompido quando o jogador perder
from random import randint
soma = 0
vitoria = 0
while True:
    computador = randint(0, 11)
    n1 = int(input('Digite um número: '))
    while n1 < 0:
        n1 = int(input('Digite um número: '))
    escolhaUser = str(input('Par ou impar? [P/I] : ').upper() .strip())[0]
    soma = computador + n1
    print(f'você escolheu {n1} e o seu adversário {computador} que resulta em {soma}, portanto')
    if soma % 2 == 0 and escolhaUser == 'P':
        vitoria += 1
        print('Você venceu, tente  novamente')
    elif soma % 2 == 1 and escolhaUser == 'I':
        vitoria += 1
        print('Você venceu tente novamente!')
    elif soma % 2 == 0 and escolhaUser == 'I':
        break
    elif soma % 2 == 1 and escolhaUser == 'P':
        break
if vitoria > 0:
    print(f'Parabéns, você venceu {vitoria} vezes e infelizmente perdeu agora.')
else:
    print('Infelizmente, você perdeu')
