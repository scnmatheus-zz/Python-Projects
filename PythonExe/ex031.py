#DESAFIO 31 DESENVOLVA UM PROGRAMA QUE PERGUNTE A VIAGEM EM KM´S, SENDO QUE:
#ATÈ 200 KM O PREÇO È FIXO DE 0.50R$ E 0.45R$ ACIMA DE 200KM

viagem = int(input('Digite a distancia em KMS de sua viagem desejada: '))

if viagem <= 200:
    custo = viagem * 0.50
    print(f'O preço de sua viagem será de R${custo:.2f}')
else:
    custo = viagem * 0.45
    print(f'O preço de sua viagem será de R${custo:.2f}')
