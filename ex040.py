# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
nota1=float(input('Insira a nota da B1... '))
nota2=float(input('Insira a nota da B2... '))
m=(nota1+nota2)/2
if m<5.0:
    resultado='\033[0;31mReprovado!\033[m'
elif 5.0<= m <7:
    resultado = '\033[0;33mem Recuperação!\033[m'
elif m>=7.0:
    resultado = '\033[0;32mAprovado\033[m!'
print('Sua média foi {:.1f} e está {}'.format(m,resultado))