from math import radians, sin, cos, tan
'''#faça um programa que leia um ângulo e mostre o valor de seno, cosseno e tangente.'''
angulo = float(input('Digite o ângulo que você deseja'))
seno = sin((radians(angulo)))
print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O angulo de {angulo} tem o COSSENO de {cosseno}:.2f')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem a TANGENTE de {tangente}')

