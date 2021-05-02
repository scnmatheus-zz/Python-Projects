#Faça um programa e leia o ano de nascimento de um jovem, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar
#se já passou do tempo do alistamento
#O programa também deve indicar o tempo que falta ou que passou do prazo
from datetime import date
nasc = int(input('Digite o ano que você nasceu'))
ano = date.today().year
idade = ano - nasc
print(idade)

if idade == 18:
    print(f'Você completou ou irá completar {idade} anos esse ano, portanto deve se alistar ainda esse ano')
elif idade <= 17:
    print(f'Você completou ou irá completar {idade} anos esse ano, portanto não deve se alistar ainda')
else:
    print(f'Você já completou 18 anos, está atrasado, deve se apresentar em uma junta militar assim que possível!')