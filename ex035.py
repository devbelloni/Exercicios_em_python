l1 = float(input('\033[0;36;40mInsira o comprimento da primeira reta... '))
l2 = float(input('Insira o comprimento da segunda reta... '))
l3 = float(input('Insira o comprimento da terceira reta... \033[m'))

s1=l2+l3
s2=l1+l3
s3=l1+l2
if s1>l1 and s2>l2 and s3>l3:
    print('As retas com dimensões {}, {} e {} formam um triângulo.'.format(l1,l2,l3))
else:
    print('As retas com dimensões {}, {} e {} não formam um triângulo.'.format(l1,l2,l3))
