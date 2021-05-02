#Crie um programa que leia varios numerios inteiros
#so ira parar quando digitar o valor 999, que é a condição final
#mostre quantos numeros foram digitados, e qual foi a soma entre eles.
soma = quantidade = 0
while True:
    n1 = int(input('Digite um número: [999] PARA PARAR'))
    if n1 != 999:
        soma = soma + n1
        quantidade = quantidade + 1
    else:
        break
print(f'Você digitou ao todo {quantidade}, somando todos os numeros chega a {soma}')