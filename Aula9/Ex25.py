nome=str(input('Digite seu nome: ')).strip()
t=nome.title()
r='Silva' in t
print('Seu nome {} tem silva? {}'.format(t, r))