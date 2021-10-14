from datetime import date
ano=int(input('Digite um ano e direi se ele é bissexto... (Coloque 0 para analisar o ano atual!)'))
if ano==0:
    ano=date.today().year
a1=ano%4
a2=ano%100
a3=ano%400
if (a1==0 and a2!=0) or a3==0:
    print('O ano de {} é um ano BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é um ano BISSEXTO!'.format(ano))
