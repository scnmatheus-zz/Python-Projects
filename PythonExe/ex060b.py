n1 = int(input('Digite o número que deseja calcular o fatorial'))
f = 1
for c in range(n1, 1, -1):
    f = f * c
print(f'O fatorial de {n1} é de {f}')
