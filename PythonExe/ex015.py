#ESCREVA UM PROGRAMA que pergunte por quantos dias um carro foi alugado e
#quantos km foram percorridos, sabendo que o carro custa por dia R$60 e R$0.15 por KM rodado.

dias = int(input('Quantos dias o carro foi alugado'))
km = float(input('Quantos KM rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago}')
