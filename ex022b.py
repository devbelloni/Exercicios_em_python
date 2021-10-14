#18)	Crie um programa que leia o nome completo de uma pessoa e mostre:
#a)	O nome com todas as letras maiúsculas
#b)	O nome com todas as letras minúsculas
#c)	Quantas letras ao todo, sem contar os espaços
#d)	Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo... ')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome.replace(" ",""))))
print('Seu primeiro nome tem {} letras.'.format(nome.find(" ")))

# resposta do professor
nome = input('Digite seu nome completo... ').strip()
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
separa=nome.split()
print('Seu nome tem {} letras'.format(len(nome)-nome.count(" ")))
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))