#desenvolva um programa que leia quatro valores pelo teclado
#guarde-os em uma tupla, no final:
#mostre quantas vezes apareceu o valor 9.
#em que posição foi digitado o primeiro valor 3
#quanis foram os números pares

num = (int(input('Digite um número: ')),
       int(input('Digite um outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o ultimo número: ')))
if 9 in num:
    print(f'Existe {num.count(9)} valores de 9 digitados')
else:
    print('O valor 9 Não foi digitado!')
if 3 in num:
    print(f'O valor 3 foi digitado na {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado! ')
for c in num:
    if c % 2 == 0:
        print(f'Os valores pares são: {c}', end='')


