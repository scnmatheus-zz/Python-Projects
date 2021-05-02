#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
#de zero até vinte, seu programa deverá ler um número pelo teclado entre 1 a 20 e
#mostrá-lo por extenso.

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
escolhauser = 'O'
while True:
    while True:
        n1 = int(input('Digite um número entre 0 e 20'))
        if n1 >= 0 and n1 <= 20:
            print(f'Você digitou o número {cont[n1]}')
            break
    escolhauser = str(input('Deseja continuar? {S/N]').upper() .strip())
    if escolhauser == 'N':
        break