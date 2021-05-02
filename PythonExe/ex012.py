#Algoritmo que leia preço do produto e faça um desconto no preço de 5%
#vamos lá...

preco = float(input('Qual o preço do produto senhor(A) R$: '))

novo = preco - (preco*5 /100)
print(f'Parabéns, o produto que custava R${preco}, agora custará R${novo}')
