velocidade=float(input('Digite sua velocidade!'))
if velocidade >= 80:
    print('Você excedeu o limite de 80km/h e foi multado em R${:.2f}.'.format((float(velocidade-80)*7)))
else:
    print('Tenha um bom dia, dirija com segurança!')
