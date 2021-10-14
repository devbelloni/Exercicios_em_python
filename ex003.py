# para input perceber que é um número tenho que declarar o tipo da variável
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
# para somar, não preciso declara o tipo
s = n1 + n2
# type mostra o tipo de variável
print("O tipo de variável é :", type(s))
print("A soma desses números é:", s)
# usando {} e .format, consigo colocar diversas variáveis em uma só msg
print("A soma entre {} e {} é: {}".format(n1, n2, s))
