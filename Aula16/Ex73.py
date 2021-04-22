times = ('Atlético-MG', 'Internacional', 'São Paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Gremio', 'Fluminense', 
         'Bahia', 'Sport Recife', 'Corinthians', 'Fortaleza', 'Ceará SC', 'Atlético-GO', 
         'Vasco da Gama', 'Athletico-PR', 'Coritiba', 'Bragantino', 'Botafogo', 'Goiás')
print('-='*50)
print('')
print('Esses são os 5 primeiros times:', end = ' ')
for c in range(0, 5+1):
    print(times[c], end = '')
    print(', ' if c < 5 else '', end='')
print('.')
print('')
print('-='*50)
print('')
print('Os últimos 4 times são: ',end='')
for c in range(16, 20):
    print(times[c], end='')
    print(', ' if c < 19 else '', end='')
print('.')
print('')
print('-='*79)
print(f'A lista em ordem alfabetica ficaria: {sorted(times)}')
if 'Chapecoense' in times:
    print('Chapecoense está na lista')
else:
    print(f'Chapecoense não está na lista.')
