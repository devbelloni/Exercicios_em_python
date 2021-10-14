cont=1
# loop na contagem
# while cont <=10:
#    print(cont, '...', end='')
#    cont += 1
#print ('Acabou')

# loop infinito
#while True:
#    print(cont, '...', end='')
#    cont += 1
#print ('Acabou')

#loop com condiçao. o 999 é um flag
#n=0
#while n !=999:
#    n=int(input("Digite um número: "))

# Mas imagine que eu queira somar todos os valores digitados. Veja que ele soma o flag
#n=s=0
#while n !=999:
#    n=int(input("Digite um número: "))
#    s += n
#print("A soma vale {}".format(s))

# Então crio um loop infinito e uso o comando brake
n=s=0
while True:
    n=int(input("Digite um número: "))
    if n==999:
        break
    s += n
#print("A soma vale {}".format(s))
#usando as fstrings
print(f"A soma vale {s}")
print(f"A soma vale {s:20}")
print(f"A soma vale {s:^20}")
print(f"A soma vale {s:->20}")
print(f"A soma vale {s:-<20}")
print(f"A soma vale {s:-^20}")

