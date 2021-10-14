# um if é condicional simples. if e else é composta e com elif é condição aninhada

nome=str(input('Qual o seu nome? '))
if nome=='Maluco':
    print('Que nome legal')
elif nome=='Marcio Belloni':
    print('Olá professor!')
elif nome=='Maria' or nome=='João':
    print('Seu nome é bem comum no Brasil')
else:
    print('Seu nome é bem comun.')

print('Tenha um bom dia {}.'.format(nome))