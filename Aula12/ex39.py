from datetime import date
a = int(input('Digite o ano de seu nascimento: '))
t = date.today().year
i = t - a
pas= i - 18
fal= 18 - i
if i > 18:
    print('Voce deveria estar alistado, já faz {} anos.'.format(pas))
elif i < 18:
    print('Voce precisa se alistar, daqui {} anos'.format(fal))
elif i == 18:
    print('Voce precisa se alistar imediatamente.')