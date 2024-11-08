numeros=list()
while True:
    n=int(input('Digite um numero:'))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado')
    else:
        print('Valor duplicado não seram adicionados')
    opção=str(input('Quer continuar? [S/N]')).upper()
    if opção=='N':
        break
print('Você digitou os valores',end=' ')
print(sorted(numeros))