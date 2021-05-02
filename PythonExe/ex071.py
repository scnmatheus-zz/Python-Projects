#Crie um programa que simule o funcionamento de um caixa eletrônico
#no inicio pergunte ao usuário qual será o valor a se rsacado (valor inteiro)
#o programa vai informar quantas cédulas de cada valor serão entregues
#obs considere; R$ 20, R$50, R$ 10, R$ 1
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de r${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

