# faça um programa que calcule a soma de todos os numeros que são multiplos de três
# entre 1 a 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'O resultado total é {soma}')
print(f'Quantidade de números que apareceram, foi : {cont}')