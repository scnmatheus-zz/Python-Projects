#Escreva um programa que pergunte o salário de um funcionário e acrescente os seguintes aumento:
#Para salários superiores a R$1250.00, calcule um aumento de 10%
#Para os inferiores o aumento deverá ser de 15%

sal = float(input('Insira seu salário: '))

if sal >= 1251:
    aumento = sal + (sal * 10) / 100

else:
    aumento = sal + (sal * 15) / 100
print(f'Parabéns, seu salário foi ajustado, agora você receberá: R${aumento:.2f}')