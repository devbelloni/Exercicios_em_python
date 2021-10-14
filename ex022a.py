frase='Curso em Video Python'

print(frase[3:13])
# resultado (so em Vide)
print(frase[3:])
# resultado (so em Video Python)
print(frase[::2])
#resultado Croe ie yhn
print()
print()
#Para escrever um texto inteiro numa tela uso """
print("""6) Uma mola de 400 N/m de constante elástica está presa
a um bloco de 3 kg que repousa sobre um trilho de ar horizontal 
que torna o atrito desprezível. Qual distensão da mola necessária 
para dar ao bloco uma aceleração de 4 m/s2, na largada?
a. 2,0 cm
b. 2,5 cm
c. 1,7 cm
d. 4 cm
e. 3 cm""")
print()
print()
#conta os 'o' na frase
print(frase.count('o'))

#trocar parte da srting
print(frase.replace('Python','Android'))

#criando a lista
print(frase.split())

#mostrando um elemento criando a lista
print(frase.split()[0])

#mostrando um caracter de um elemento criando a lista
print(frase.split()[0][3])
