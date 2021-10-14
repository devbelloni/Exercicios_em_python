# operadores matemáticos
# + adição
# - subtração
# * multiplicação
# / divisão
# % resto
# ** potência (pode usar pow())
# // divisão inteira
a=5+2
print(a)
b=5-2
print(b)
c=5*2
print(c)
d=5/2
print(d)
e=5**2
print(e)
f=5//2
print(f)
g=5%2
print(g)

#Posso multiplicar o string com numero. "oi"*10
print("oi"*10)

# alinhamentos
nome = "Marcio"
print("oi !{:<20}!".format(nome))
print("oi !{:>20}!".format(nome))
print("oi !{:^20}!".format(nome))
print("oi !{:-^20}!".format(nome))

#casas decimais em números
d=4/3
int(d)
print('Sem controle de casas decimais: {}'.format(d))
print('Com controle de casas decimais: {:.4f}'.format(d))

# para não mudar a linha end=' '. para mudar \n
print('Sem controle de casas \n decimais: {}'.format(d), end=' ')
print('Com controle de casas \n decimais: {:.4f}'.format(d))

