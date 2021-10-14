# sorteio de nomes com random
import random
n1 = input('Primeiro nome...')
n2 = input('Segundo nome...')
n3 = input('Terceiro nome...')
n4 = input('Quarto nome...')
nomes=(n1,n2,n3,n4)
n=random.choice(nomes)
print('O nome escolhido foi: {}.'.format(n))