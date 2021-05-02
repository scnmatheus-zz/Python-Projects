#Acompanhe o principio matemático, capaz de formar um triangulo e pergunte ao usuário
#O tamanho de tres retas e diga se é possível formar um triangulo

r1 = float(input('Digite a base do triangulo: '))
r2 = float(input('Digite um lado do triângulo: '))
r3 = float(input('Digite o outro lado do triângulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os SEGMENTOS ACIMA podem formar um triângulo')
else:
    print('Os seguimentos acima não podem formar um triângulo')




