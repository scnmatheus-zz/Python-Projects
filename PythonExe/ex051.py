#faça o programa que leia o primeiro termo e a razão de uma PA
#no final mostre os 10 primeiros termos dessa progressão.

print('-=-'*12)
print('==============PROGRESSÂ ARITMÈTICA=============')
print('-=-'*12)
começo = int((input('Começo da contagem: ')))
fim = int(input('de quantos em quantos: '))
decimo = começo + (10-1)*fim

for c in range(começo, decimo + fim, fim):
    print(c, end='-')