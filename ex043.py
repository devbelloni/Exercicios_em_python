# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice
# de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
peso = float(input('Apresente seu peso ... '))
altura = float(input('Apresente sua altura ... '))
imc=peso/(altura**2)
if imc<18.5:
    status='abaixo do peso'
elif 18.5<=imc<25:
    status='peso ideal'
elif 25<=imc<30:
    status='sobrepeso'
elif 30<=imc<40:
    status='obesidade'
elif imc > 40:
    status='obesidade mórbida'
print('Para seu peso de {}kg e altura de {}m, você possui IMC {:.1f} e encontra-se em {}.'.format(peso, altura, imc, status))
