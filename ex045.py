# Crie um programa que faça o computador jogar Jokenpô com você.
import random
import time
menu=['0','pedra','papel','tesoura']
print('\033[1;36mX' * 43)
print('XX \033[1;0;45mVAMOS JOGAR "PEDRA - PAPEL - TESOURA?\033[m\033[1;36m XX')
print('X' * 43)
jogador = int(input('''\033[mEscolha a sua opção:
1) Pedra
2) Papel
3) Tesoura\n'''))
print('\033[1;36mX' * 7)
print('X\033[m JO  \033[1;36mX ')
time.sleep(1)
print('X\033[m KEN \033[1;36mX ')
time.sleep(1)
print('X\033[m PÔ  \033[1;36mX ')
print('\033[1;36mX\033[m' * 7)

time.sleep(1)

computador = random.randint(1, 3)
if computador == 1:
    if jogador == 1:
        jogada = 'Empatamos'
    elif jogador == 2:
        jogada = 'Jogador venceu'
    elif jogador == 3:
        jogada = 'Computador venceu'
    else:
        jogada = 'Operação inválida'
elif computador == 2:
    if jogador == 2:
        jogada = 'Empatamos'
    elif jogador == 3:
        jogada = 'Jogador venceu'
    elif jogador == 1:
        jogada = 'Computador venceu'
    else:
        jogada = 'Operação inválida'
elif computador == 3:
    if jogador == 3:
        jogada = 'Empatamos'
    elif jogador == 1:
        jogada = 'Jogador venceu'
    elif jogador == 2:
        jogada = 'Computador venceu'
    else:
        jogada = 'Operação inválida'
print('Eu escolhi {} e você escolheu {}. Resutado: {}. '.format(menu[computador], menu[jogador], jogada))
input()