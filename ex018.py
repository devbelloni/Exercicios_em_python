# Lê um ângulo qualquer e mostra seno, cosseno e tangente.
import math

n=float(input('Digite um ângulo qualquer... '))
ang=n*math.pi/180
sen=math.sin(ang)
cos=math.cos(ang)
tg=math.tan(ang)
print('O seno do ângulo {}° é {}, o cosseno é {:.3f} e a tangente é {:.3f}'.format(n,sen,cos,tg))

# resposta do professor
n=float(input('Digite um ângulo qualquer... '))
sen=math.sin(math.radians(n))
cos=math.cos(math.radians(n))
tg=math.tan(math.radians(n))
print('O seno do ângulo {}° é {}, o cosseno é {:.3f} e a tangente é {:.3f}'.format(n,sen,cos,tg))
