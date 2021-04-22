print('Calculadora de IMC.')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura*2)
if imc <= 18.5:
    print(f'Seu IMC é {imc:.2f} você está abaixo do peso.')
elif imc > 18.5 or imc <= 25:
    print(f'Seu IMC é {imc:.2f} Parabéns, você está no peso ideal.')
elif imc > 25 or imc <= 30:
    print(f'Seu IMC é {imc:.2f}, Cuidado, você está com sobrepeso.')
elif imc > 30 or imc <= 40:
    print(f'Seu IMC é {imc:.2f}, O amigão, tu tá com obesidade.')
else:
    print(f'Seu IMC é {imc:.2f}, KRAI MALUCO, PARA DE COMER IMEDIATAMENTE.')
