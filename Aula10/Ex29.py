v=int(input('Digite a velocidade de seu carro: '))
print('Parado senhor, deixe-me analisar sua vecolidade.')
if v < 80:
    print('Pode continuar senhor, você está dentro da lei, porém irei continuar de olho em você.')
else:
    print('STOP RIGHT THERE YOU CRIMINAL SCUM, você estava a {}Km/s'.format(v))
    m=(v-80)*7
    print('Você terá que pagar esta multa no valor de R${}, se quiser continuar rodando por aí.'.format(m))
