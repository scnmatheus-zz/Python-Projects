#Crie um programa que leia vários números inteiros no teclado, o programa
#Só vai parar quando o usuário digitar o valor 999, no final mostre quanto foi a soma
#dos valores digitados. e quantos foram digitados.
soma = 0
num = 0
n1 = 0
while n1 != 999:
    n1 = int(input('Digite um número: [999] para PARAR: '))
    if n1 != 999:
        soma = soma + n1
        num = num + 1
print(f'Ao todo foram {num} digitados, com a soma total de {soma}')