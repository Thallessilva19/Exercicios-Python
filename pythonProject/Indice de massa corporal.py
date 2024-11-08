peso=float(input('Qual é o seu peso:'))
altura=float(input('Qual a sua altura:'))
imc=peso/(altura**2)

if imc <=18.5:
    print('Você está abaixo de peso ideal')
elif imc ==18.5 or imc<=25:
    print('Você está no peso ideal')
elif imc ==25.1 or imc<=30:
    print('Você está sobrepeso')
elif imc ==30.1 or imc<=40:
    print('Você está obeso')
elif imc>40:
    print('Você está em obesidade mórbida')
print('O seu IMC é {}'.format(imc))
