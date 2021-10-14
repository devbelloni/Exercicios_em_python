cidade=input('Escreva o nome da sua cidade...').strip()
c=cidade.find(" ")
cidade=cidade.lower()
print('Esta cidade começa com o nome "Santo"? {}.'.format('santo' in cidade[0:c]) )

# RESPOSTA DO PROFESSOR
print(cidade[:5].upper() == 'SANTO')