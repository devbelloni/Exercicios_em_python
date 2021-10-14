frase=input('Escreva uma frase...\n').lower().replace('á','a').replace('ã','a').replace('â','a').strip()
print("""A letra "a" aparece {} vezes,
sendo que aparece na primeira vez na 
posição {} e na última vez, na 
posição {}".""".format(frase.count("a"), frase.find("a")+1,frase.rfind("a")+1))