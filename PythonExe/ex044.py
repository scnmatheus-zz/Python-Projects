#Elabore um programa que calcule o valor a ser pago por um produto considerando a forma:
# A vista: dinheiro/cheque: 10% de desconto
#A vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor do produto R$ '))
print('[1] para pagar a vista no dinheiro/cheque 10% desc [2] para pagar no cartão a vista 5% desc')
forma = int(input('[3] para pagar em 2x no cartão (preço normal) e [4] 3x ou mais (20% juros) '))

if forma == 1:
    novopreco = preco - (preco*10/100)
elif forma == 2:
    novopreco = preco - (preco*5/100)
elif forma == 3:
    novopreco = preco
elif forma == 4:
    novopreco = preco + (preco*20/100)

print(f'O valor total a ser pago sera de {novopreco}')