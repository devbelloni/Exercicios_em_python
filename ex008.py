n=float(input('Digite um número em metros e mostrarei ele em centímetros e milímetros.  '))
cm=n*100
mm=n*1000
print('O número digitado de {}m corresponde à {:>5}cm e à {:>5}mm.'.format(n, cm, mm))