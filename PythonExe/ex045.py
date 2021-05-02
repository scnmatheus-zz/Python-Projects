#Crie um programa que faça o computador jogar jokenpô com você.
from random import choice
from time import sleep
escolhapc = ['pedra', 'papel', 'tesoura']
jogo = choice(escolhapc)
print('-=-'*10)
print('-=-=-=-=-=-=-JOKENPÔ-=-=-=-=-=')
print('Jogue contra o computador, escolha entre pedra, papel e tesoura')
escolhausuario = str(input('Escolha [PAPEL] | [PEDRA] | [TESOURA] : ') .lower() .strip())
sleep(1)
print('O computador está a decidir sua jogada, aguarde..')
print('PROCESSANDO...')
sleep(2)
print(f'O computador escolheu: {jogo}')
sleep(1)
if escolhausuario == 'papel' and jogo == 'pedra':
    print('Parabéns, você venceu!!')
elif escolhausuario == 'papel' and jogo == 'tesoura':
    print('Lamento, você perdeu..')
elif escolhausuario == 'papel' and jogo == 'papel':
    print('Empatou!!')
elif escolhausuario == 'tesoura' and jogo == 'papel':
    print('Parabéns, você venceu')
elif escolhausuario == 'tesoura' and jogo == 'pedra':
    print('lamento, você perdeu..')
elif escolhausuario == 'tesoura' and jogo == 'tesoura':
    print('Empatou!!')
elif escolhausuario == 'pedra' and jogo == 'tesoura':
    print('Parabéns, você venceu!!')
elif escolhausuario == 'pedra' and jogo == 'papel':
    print('Lamento, você perdeu..')
elif escolhausuario == 'pedra' and jogo == 'pedra':
    print('Empatou!!') 