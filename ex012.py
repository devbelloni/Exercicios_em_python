p=float(input('Qual o preço do produto?  '))
v= p*(1-0.05)
print('O preço do produto é de R${:.2f} e com 5% de desconto fica R${:.2f}.'.format(p,v))