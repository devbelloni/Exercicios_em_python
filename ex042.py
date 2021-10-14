# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
# triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
l1 = float(input('\033[0;36;40mInsira o comprimento da primeira reta... '))
l2 = float(input('Insira o comprimento da segunda reta... '))
l3 = float(input('Insira o comprimento da terceira reta... \033[m'))
s1=l2+l3
s2=l1+l3
s3=l1+l2
if s1>l1 and s2>l2 and s3>l3:
    if l1==l2 and l1==l3 and l3==l2:
        print('As retas com dimensões {}, {} e {} formam um triângulo equilátero.'.format(l1,l2,l3))
    elif l1!=l2 and l1!=l3 and l3!=l2:
        print('As retas com dimensões {}, {} e {} formam um triângulo escaleno.'.format(l1,l2,l3))
    elif (l1==l2 and l1!=l3 and l3!=l2)or (l1!=l2 and l1==l3 and l3!=l2)or (l1!=l2 and l1!=l3 and l3==l2):
        print('As retas com dimensões {}, {} e {} formam um triângulo isóceles.'.format(l1,l2,l3))
else:
    print('As retas com dimensões {}, {} e {} não formam um triângulo.'.format(l1,l2,l3))
input()