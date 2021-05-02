#Crie um programa que leia o nome completo de uma pessoa e mostre:

#Todas as letras maiúsculas

#Todas as letras minúsculas

#Quantas letras ao máximo sem considerar os espaços

#quantas letras tem o nome

nome = str(input('Digite seu nome: ').strip())
print(f'Seu nome em maiúscula é {nome.upper()}')
print(f'Seu nome em Minúscula é {nome.lower()}')
espacos = len(nome) - nome.count(' ')
print(f'A quantidade de caracteres no seu nome é {espacos}')
primeiro = nome.find(' ')
print(f'Seu primeiro nome tem {primeiro} Letras')