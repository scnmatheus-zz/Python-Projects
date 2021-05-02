#Faça um programa que mostte o primeiro e ultimo nome de uma pessoa.

nome = str(input('Digite seu nome completo: ' .strip()))
n = nome.split()
print('Muito Prazer em te Conhecer')
print(f'Primeiro Nome: {n[0]}')
print(f'Ultimo nome: {n[-1]}')