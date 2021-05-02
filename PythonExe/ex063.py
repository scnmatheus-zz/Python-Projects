#Escreva um programa que leia um numero n inteiro, qualquer e mostre na tela os
# n primeiros elemenetos de uma sequência de fibonnaci.
print('-=-'*9)
print('-=-=-=-=FIBONACCI')
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} -> {t2} ',end='')
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3} ', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1