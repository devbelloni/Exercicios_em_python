nome=input('Escreva Seu nome completo...\n')
n1=nome.find(" ")
n2=nome.rfind(" ")
print("Seu primeiro nome é: {}".format(nome[:n1]))
print("Seu último nome é: {}".format(nome[n2:]))