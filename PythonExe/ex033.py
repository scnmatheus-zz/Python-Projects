# ESCREVA UM PROGRAMA QUE RECEBA TRÊS NÚMEROS E INDIQUE O MAIOR

a = float(input('Digite o primeiro número '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')
