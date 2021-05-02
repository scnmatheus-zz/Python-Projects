#Algoritmo que aumente o salário de um determinado funcionário em #15%

nome = input('Seja muito bem vindo(A), por favor diga-nos, qual o seu nome? ')
sal = float(input(f'Perfeito, {nome}, agora por favor nos diga, qual o seu salário? R$: '))
novo = sal + (sal * 15 / 100)

print(f'Parabéns, com sua promoção, seu salário foi ajustado para R$:{novo:.2f}')