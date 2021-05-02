#Faça um programa que mostre a tabuada de varios numeros, um de cada vez
#só deve parar quando o usuário digitar um valor negativo
tabuada = 0
while True:
    n1 = int(input('Digite um número: '))
    if n1 >= 0:
        for c in range(0, 11):
            tabuada = n1 * c
            print(f'{n1} X {c} = {tabuada}')
    if n1 < 0:
        break
print('fim')