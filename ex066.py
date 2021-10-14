# Crie um programa que leia vários números inteiros pelo teclado. O número somente vai para quando o usuário
# digitar 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma
# entre eles desconsiderando o flag.

n=s=0
cont=0
while True:
    n=int(input(("Insira um número inteiro (999 para):")))
    if n==999:
        break
    cont+=1
    s+=n

print (f"Você inseriu {cont} números e a soma é {s}.")

