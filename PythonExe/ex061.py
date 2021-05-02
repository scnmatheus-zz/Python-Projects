#Refaça o desafio 051, lendo o primeiro termo e razão de uma PA, mostrando os
#10 primeiros termos usando o while
print('Gerador de PA')
print('-=-'*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end='-')
    termo = termo + razao
    cont = cont + 1
