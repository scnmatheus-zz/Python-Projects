#faça um programa que leia um número qualquer e mostra o seu fatorial
n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print('Calculando o fatorial ')
while c > 0:
    print(f'{c}',end='')
    print('x' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f'O fatorial é de {f}')