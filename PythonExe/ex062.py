#melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos
#o progra,a encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-=-'*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end='-')
        termo = termo + razao
        cont = cont + 1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

