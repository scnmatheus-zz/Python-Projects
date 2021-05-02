#faça um programa que leia  o sexo e uma pessoa, mas só aceite os valores 'M' ou 'F'
#caso esteja errado. peça a digitação novamente até ter um valor correto.
s = 'a'
while s != 'm' and 'f':
    s = str(input('Digite seu Sexo: [M/F] : ').lower())
    if s != 'm' and s != 'n':
        print('Dados inváldios, por favor, tente novamente.')
print('fim')