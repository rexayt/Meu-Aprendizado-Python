#calcular IMC
#IMC = Peso / (Altura * Altura)
a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
i = p / (a*2)
if i < 18.5:
    print('Ih rapaz, você está abaixo do seu peso ideal, seu IMC é {:.2f}.'.format(i))
elif i > 18.5 and i < 25:
    print('Ae sim, você tá no peso ideal. seu IMC é {:.2f}.'.format(i))
elif i > 25 and i < 30:
    print('Você tá com um leve sobrepeso amigão, seu IMC é {:.2f}'.format(i))
elif i > 30 and i < 40:
    print('Tu tá obeso mlk, sai daqui e vai fazer exercício, seu IMC é {:.2f}.'.format(i))
else:
    print('Tu tem obesidade mórbida, vai fazer um tratamento cara, seu IMC é {:.2f}'.format(i))
