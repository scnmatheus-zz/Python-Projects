print('=============CALCULOMÊTRO==========')
met = float(input('Bem vindo, senhor(A), quantos M, sua casa tem de base ? '))
larg = float(input('Quantos M de altura, sua casa tem? '))

area = met*larg
perim = met+larg+met+larg

print(f'Perfeito, chegamos ao resultado, sua casa tem {area}M de área e {perim}M de perimêtro ')

tint = area / 2

print(f'Considerando que você tem {area}M de área, precisará de {tint}M', end=' ')
print('Em titnta para poder pintar toda sua parede')
