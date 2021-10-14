# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n=int(input('\033[2;34;43mEscreva um número inteiro.\033[m'))
s=int(input(
"""Selecione a base para conversão:
\033[2;37m[1] binário\033[m
\033[2;35m[2] octal\033[m
\033[2;34m[3] hexadecimal\033[m
"""))
if s==1:
    print('\033[2;37mO número {} em Binário é igual à "{}".\033[m'.format(n, bin(n)))
elif s==2:
    print('\033[2;35mO número {} em Octal é igual à "{}".\033[m'.format(n, oct(n)))
elif s==3:
    print('\033[2;34mO número {} em Hexadecimal é igual à "{}".\033[m'.format(n, hex(n)))
