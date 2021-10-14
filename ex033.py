n1=int(input('Digite o primeiro número... '))
n2=int(input('Digite o segundo número... '))
n3=int(input('Digite o terceiro número... '))
r='O primeiro'
if n2>n1 or n2>n3:
    r='O segundo'
if n3>n1 or n3>n2:
    r='O terceiro'
if n1==n2==n3:
    r='Nenhum'
print('{} número é o maior.'.format(r))

