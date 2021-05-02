n = 1
pares = 0
impares = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            pares = pares + 1
        elif n % 2 == 1:
            impares = impares + 1
print(f'Você digitou numeros {pares} e digitou numeros {impares} impares ')