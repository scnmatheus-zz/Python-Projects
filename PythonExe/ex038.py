#Escreva um programa que leia dois números inteiros e compare-os
# indicando qual o maior número, menor ou se são iguais

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}')
elif num2 > num1:
    print(f'O número: {num2} é maior que o número {num1}')
else:
    print('os dois valores são IGUAIS')