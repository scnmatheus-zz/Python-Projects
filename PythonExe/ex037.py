#escreva um programa que leia um número inteiro qualquer e peça a base para qual o usuario
#deseja como conversão: 1 - para binário 2 - para octal 3 - para hexadecimal
num = int(input('digite um número inteiro: '))
print('''Escolha uma das bases para conversão: )
[1] Converter para BINÀRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Sua escolha:'))
if opcao == 1:
    print(f'{num} convertido para binário é igual á {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('opção invalida, tente novamente.')
