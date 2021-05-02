#desenvolva um programa que leia seis números inteiros e mostre a soma somente dos
#numeros pares, os imperes devem ser desconsiderados
soma = 0
for c in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
print(f'O resultado total dessa soma é de: {soma}')