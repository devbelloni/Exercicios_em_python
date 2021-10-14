# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
valor = float(input('Indique o valor do produto ...\n'))
pagamento = int(input("""\033[1;34mInquique o modo de pagamento como abaixo:
1) Dinheiro / Cheque
2) Cartão à vista
3) 2x no Cartão
4) 3 x ou mais no Cartão\n\033[m"""))
if pagamento == 1:
    preço = valor * (1 - 0.1)
    f = 'Dinheiro / Cheque'
elif pagamento == 2:
    preço = valor * (1 - 0.05)
    f = 'Cartão à vista'
elif pagamento == 3:
    preço = valor
    f = '2 x no Cartão'
elif pagamento ==4:
    preço = valor * (1 + 0.2)
    f = '3 x ou mais no Cartão'
else:
    print('Opção inválida de pagamento. Tente novamente!')
    preço = 0
    f = 'ERRO'

print('Para pagamento em {}, o valor do produto será R${:.2f}.'.format(f, preço))
