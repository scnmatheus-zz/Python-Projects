#crie um programa que leia a idade e sexo de várias pessoas, a cada pessoa cadastrada
#deve perguntar se o usuário quer ou não continuar
# no final mostre:

#quantas pessoas tem mais de 18 anos
#quantos homens foram cadastrados
#quantas mulheres tem menos de 20 anos.

from datetime import datetime
from time import sleep
totMaior = 0
maiores = 0
menores = 0
homens = 0
mulheres = 0
totMulheres = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F] : ').upper() .strip())[0]
    if idade > 18:
        totMaior = totMaior + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        totMulheres = totMulheres + 1
    escolhaUser = str(input('Deseja continuar? [S/N]').upper() .strip())[0]
    if escolhaUser == 'N':
        break
print(f'Ao todo existem {totMaior} maiores de 18 anos, {homens} homens foram cadastrados\n',end='')
print(f'{totMulheres} mulheres são menores de 20 anos')
