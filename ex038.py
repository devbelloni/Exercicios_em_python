# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
n1=float(input('Insira um número... '))
n2=float(input('Insira outro número... '))
if n1>n2:
    print('O primeiro valor é maior que o segundo valor. ')
elif n1 < n2:
    print('O segundo valor é maior que o primeiro valor. ')
else n1 == n2:
    print('Os dois valores são iguais. ')