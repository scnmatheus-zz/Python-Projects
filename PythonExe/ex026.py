#Crie um programa que leia uma frase e mostre: quantas vezes aparece a letra "A"
#em que posição aparece a primeira vez, em que posição pela ultima

nome = str(input('Digite seu nome')).lower() .strip()

print(f'A quantidade de letras A no seu nome é: {nome.count("a")}')
print(f'A primeira vez que a letra A aparece é em: {nome.find("a")+1}')
print(f'A ultima letra A aparece na posicao {nome.rfind("a")+1}')

