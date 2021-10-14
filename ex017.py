# Programa que pede o cateto oposto e adjacente e calcula a hipotenusa de um triângulo retânculo
import math
ca = float(input('Digite o cateto adjacente ao ângulo... '))
co = float(input('Digite o cateto oposto ao ângulo... '))
h=math.sqrt((ca**2)+(co**2))
ang=(math.atan(co/ca)*180/math.pi)
print('A hipotenusa é de {} e o ângulo é de {}°.'.format(h,ang))

# resposta do professor
ca = float(input('Digite o cateto adjacente ao ângulo... '))
co = float(input('Digite o cateto oposto ao ângulo... '))
print('A hipotenusa é de {}.'.format(math.hypot(ca,co)))
