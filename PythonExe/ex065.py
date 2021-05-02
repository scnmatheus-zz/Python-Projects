#crie um programa que leia varios numeros inteiros pelo teclado, no final
#deve mostrar a média entre todos os valores e qual foi o maior e menor valor digitado
#o programa deve perguntar se deseja continuar ou não digitando valores
resp = 'S'
soma = 0
quantidade = 0
media = 0
menor = 0
maior = 0
while resp != 'N':
    n1 = int(input('Digite um número: '))
    resp = str(input('Deseja continuar? [S/N]').strip().upper())[0]
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = n1
        menor = n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    soma = soma + n1
    if resp == 'S':
        media = soma / quantidade
print(f'O maior número digitado foi: {maior} e o menor foi {menor}')
print(f'A media entre {soma} é de {media} e a quantidade total de números foi {quantidade}')