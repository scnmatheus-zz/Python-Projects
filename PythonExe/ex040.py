#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem:
#Média abaixo de 5.0 Reprovado
#media entre 5.0 e 6.7 recuperação
#7.0 ou superior, aprovado

n1 = float(input('Digite sua primeira nota; '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print('Aluno reprovado')
elif media <= 6.9:
    print('Aluno em recuperação')
else:
    print('Aluno aprovado')