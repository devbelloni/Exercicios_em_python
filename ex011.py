h=float(input('Digite a altura da parede em metros... '))
l=float(input('Digite a largura da parede em metros... '))
a=h*l
t=a/2
t=round(t+0.5)
print('A parede de argura {}m e altura {}m possui área de {}m² e necessitará de {}L de tinta.'.format(l,h,a,t))