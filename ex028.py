from random import randint
from time import sleep
n=(randint(0,10))
a=int(input('Advinhe o número que estou pensando de 0 à 10...\n Digite o número abaixo... \n'))
print('PROCESSANDO...')
sleep(2)
if a==n:
    print('Você acertou! O número que pensei foi {}!'.format(n))
else:
    print('Você Errou. Eu pensei no número {} e você digitou {}.'.format(n,a))
