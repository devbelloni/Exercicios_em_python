#Crie um programa que leia um numero real pelo teclado e mostre o seu inteiro
import math

r=float(input('Digite um número real... '))
r1 = math.ceil(r)
r2 = math.floor(r)
r3 = math.trunc(r)
print('O número {} tem a parte inteira {}'.format(r,r3))
print('O valor digitado foi {}.\nArredondando para cima: {}.\nArredondando para baixo: {}.\nEliminando a vírgula: {}.'.format(r, r1,r2,r3))
