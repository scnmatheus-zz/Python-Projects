import math
'''faça um programa que leia o comprimento do cateto oposto e do cateto adjcanete de um triângul
#e mostre o comprimento da hipotenusa'''

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h1 = math.hypot(co, ca)

