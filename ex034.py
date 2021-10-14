sal=float(input('Qual o salário do funcionário?'))
if sal>1250.00:
    p='10%'
    au=sal*(1+0.1)
else:
    p = '15%'
    au = sal * (1 + 0.15)

print('O salário de R${:.2f} receberá um aumento de {} e irá para R${:.2f}. '.format(sal,p,au))