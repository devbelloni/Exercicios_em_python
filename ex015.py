km=float(input('Digite a quantidade de kilômetros percorridos... '))
d=float(input('Digite a quantidade de dias que o carro foi alugado... '))
p=(km*0.15)+(d*60)
print('O valor à pagar por {} dias e {}km rodados será de: R${:.2f}'.format(d, km, p))