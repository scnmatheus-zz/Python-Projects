#Desenvolva uma Lógica que leia o peso e altura de uma pessoa e mostre o seu IMC
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obseridade mórbida

peso = float(input('Qual é seu peso? KG: '))
altura = float(input('Qual é sua altura? M: '))

imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif imc >= 18.5 and imc < 25:
    print('Essa pessoa está no peso normal!')
elif imc >= 25 and imc <= 30:
    print('Você está em sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('Você está em OBSEIDADE, cuidado!')
elif imc >= 40:
    print('Você está em obesidade mórbida!!')