cont=0
lista=[]
while True:
    numero=int(input('Digite um valor:'))
    lista.append(numero)
    cont+=1
    print('Valor adicionado a lista')
    opçao=str(input('Quer continuar? [S/N]')).upper()
    if opçao!='S':
        break
print(f'foram digitados {cont} numeros')

if 5 not in lista:
        print('Na lista não tem o numero 5')
else:
        print('Na lista tem o numero 5')
lista.sort(reverse=True)
print(f'Os numeros de forma decrescente é {lista}')


