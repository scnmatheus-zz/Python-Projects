#DESAFIO 029, ESCREVA UM PROGRAMA QUE CALCULE A VELOCIDADE DO CARRO
# SE ULTRAPASSAR 80 KM/H RECEBERA UMA MULTA, ONDE A CADA KM EXTRA, A MULTA ADICIONA 7 REAIS
veloc = int(input('Digite a velocidade do carro'))
if veloc >= 81:
    multa = (veloc-80)*7
    print(f'O valor da sua multa é R${multa:.2f}')
else:
    print('Parabéns, você não foi multado!')
print('---Fim---')