#faça um programa que leia um número inteiro e diga se ele é ou não um número primo
primo = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    print(c, end='-')
    if num % c == 0:
        primo = primo + 1
if primo == 2:
    print(f'\n{num} é primo')
else:
    print(f'\n{num} Não é primo')
