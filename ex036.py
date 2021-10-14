# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

v=float(input('Qual o valor da casa?'))
s=float(input('Qual o valor do salário do comprador?'))
t=float(input('Qual o tempo do parcelamento em anos?'))

p=v/(t*12)
if p>(s*0.3):
    print('Seu salário não aprova o financiamento. Tente compor renda.')
else:
    print('Parabéns! Seu financiamento será aprovado.')