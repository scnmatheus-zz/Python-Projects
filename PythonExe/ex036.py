#Crie um programa para aprovar um empréstimo bancário para a compra de uma casa
#O programa deve perguntar: O valor da casa, o salário do comprador, quantos anos vai pagar
#Calcule a prestação mensal sabendo que ela não pode exceder 30% do salário ou o empréstimo será negado

sal = float(input('Digite seu salário : '))
valorcasa = float(input('Digite o valor da residência que deseja financiar: '))
anuidade = int(input('Em quantos anos você irá pagar? : '))
mensalidade = anuidade * 12
valortotal = valorcasa / mensalidade
capital = (sal * 30 / 100)
if valortotal <= capital:
    print(f'Parabéns, sua casa foi financiada em aproximadamente {mensalidade} meses ',end=" ")
    print(f'Pelo valor de R${valortotal:.2f} mensalmente.')
else:
    print('Infelizmente você não pode financiar a casa')

