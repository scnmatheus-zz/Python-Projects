#crie um programa que leia doiss valores e mostre um menu na tela
#[1] para somar
#[2] para multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa
#o programa deve realizar a operação solicitada em cada caso.
op = 0
soma = 0
multiplo = 0
while op != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    op = int(input('''
             [1] para somar
             [2] para multiplicar
             [3] para maior
             [4] novos numeros
             [5] sair do programa'''))
    if op == 1:
        soma = n1 + n2
        print(f'O valor da soma entre {n1} e {n2} é igual a {soma}')
    elif op == 2:
        multiplo = n1 * n2
        print(f'O resultado da multplicação entre {n1} e {n2} é igual á {multiplo}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        elif n1 == n2:
            print(f'Os valores são iguais!')
    elif op == 4:
        print('Informe os números novamente...')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('programa finalizado!')
    else:
        print('Opção invalida, tente novamente.')
        print('-=-'*8)