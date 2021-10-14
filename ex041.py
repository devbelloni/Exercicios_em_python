# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
print('\033[1;35m*'*36)
print('*\033[m CONFEDERAÇÃO NACIONAL DE NATAÇÃO \033[1;35m*')
print('\033[1;35m*\033[m'*36)
ano=int(input('Qual o ano de nascimento do atleta? '))
idade=date.today().year-ano
if idade<=9:
    cat='mirim'
elif idade<=14:
    cat='infantil'
elif idade<=19:
    cat='júnior'
elif idade<=20:
    cat='sênior'
else:
    cat='master'
print('O atleta possui {} anos e está inserido na categoria {}. '.format(idade,cat))

