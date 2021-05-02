#Crie um programa e leia o ano de nascimento de um atelta e mostre sua categoria
#Até 9 anos: MIRIM
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 20 anos: S~enior
#Acima: Master
from datetime import date
nasc = int(input('Digite o ano que você nasceu: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('O atleta é de categoria mirim ')
elif idade <= 14:
    print('O atleta é de categoria infantil ')
elif idade <= 19:
    print('O atleta é de categoria júnior ')
elif idade <= 25:
    print('O atleta é de categoria sênior')
elif idade > 25:
    print('O atleta é Master ')

print(f'A idade é {idade}')