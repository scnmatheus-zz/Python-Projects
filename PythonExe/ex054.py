#crie um programa que leia o ano de nascimento de 7 pessoas
#no final mostre quantas pessoas atingiram a maioridade e quantas não atingiram
#considere a maioridade com 21 anos
from datetime import date
maior = 0
menor = 0
for c in range (0, 7):
    nasc = int(input('Digite o ano que nasceu'))
    if 2021 - nasc >= 21:
        maior = maior + 1
    elif 2021 - nasc <= 20:
        menor = menor + 1
print('-=-'*12)
print(f'A quantidade de maiores de idade é no total de {maior}')
print(f'Enquanto a quantidade de menores de idade é de no total {menor}')
print('-=-'*12)