#crie um programa que leia o nome e o preço de varios produtos
#dever perguntar se o usuário quer continuar, no final mostre:

#qual é o total gasto nas compras

# quantos produtos custam mais de R$ 1000

#qual o nome do produto mais barato?
print('-=-'*10)
print('     MERCADÂO BARATO     ')
print('-=-'*10)
preco = 0
menor = 0
maior = 0
soma = 0
quant = 0
menorproduto = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o valor do produto R$: '))
    soma = soma + preco
    quant = quant + 1
    if quant == 1:
        maior = preco
        menor = preco
    if preco > maior:
        maior = preco
    if preco < menor:
        menor = preco
        menorproduto = produto
    parar = str(input('Deseja parar? [S/N] : ').upper() .strip())[0]
    if parar == 'S':
        break
print(f'a soma dos produtos comprado foi de R${soma} \n o produto mais caro foi {maior}\n',end='')
print(f'O produto mais barato foi {menor} e era o {menorproduto}')