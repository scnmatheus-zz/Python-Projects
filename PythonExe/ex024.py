#Crie um programa que leia o nome de uma cidade, e ele vai dizer se começa ou não
#Com a palavra "SANTO"

nasc = str(input('Digite a cidade que você nasceu: ')) .strip()
print(nasc[:5].upper() == 'SANTO')

