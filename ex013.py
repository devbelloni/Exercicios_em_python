p=float(input('Qual o salário do funcionário?  '))
v= p*(1+0.15)
print('O valor do salário é de R${:.2f} e com 15% de aumento ficará R${:.2f}.'.format(p,v))