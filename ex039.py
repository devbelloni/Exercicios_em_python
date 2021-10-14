# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano=int(input('Qual o ano de nascimento? '))
idade=date.today().year-ano
if idade==18:
    print('\033[1;33mEsse ano você fará {} anos e deve se alistar! \033[m'.format(idade))
elif idade>18:
    print('\033[1;31mEsse ano você fará {} anos já deveria ter se alistado!\033[m'.format(idade))
elif idade<18:
    print('\033[1;32mEsse ano você fará {} anos e ainda vai se alistar!\033[m'.format(idade))

# solução do professor
from datetime import date
atual=date.today().year
nasc=int(input('Solução do professor:\nAno de Nascimento:'))
idade=atual-nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18-idade
    print('Ainda faltam {} anos para o alistmento.'.format(saldo))
    ano=atual+saldo
    print('Seu alistamento foi em {}.'.format(ano))
elif idade >18:
    saldo=idade-18
    print('Você já deveria ter se alistado á {} anos.'.format(saldo))
    ano=atual-saldo
    print('Seu allistamento foi em {}.'.format(ano))