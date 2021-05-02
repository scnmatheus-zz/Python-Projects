#faça um programa que leia um ano qualquer e diga se ele é bissexto
from datetime import date
ano = int(input('Digite o ano que quer analisar? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')