n=float(input('Digite a distância percorrida em km...  '))
if n<=200:
    n=n*0.5
    print('Sua passagem é de R${:.2f}'.format(n))
else:
    n = n * 0.45
    print('Sua passagem é de R${:.2f}'.format(n))
