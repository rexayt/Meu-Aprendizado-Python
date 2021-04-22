nome=str(input('Digite uma frase: ')).strip()
a=nome.upper()
po1=a.find('A')+1
po2=a.rfind('A')+1
print('A letra "A", aparece {} vezes na frase.'.format(a.count('A')))
print('A letra "A", aparece pela primeira vez na {} posição da frase.'.format(po1))
print('A letra "A", aparece pela última vez na {} posição da frase.'.format(po2))