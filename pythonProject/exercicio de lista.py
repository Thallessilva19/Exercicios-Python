lista=[]
pares=[]
impar=[]
while True:
    user=int(input('Digite um numero:'))
    print('=-'*15)
    lista.append(user)
    opcao=str(input('Quer continuar? [S/N]')).upper()
    print('=-' * 15)
    if opcao!='S':
        break
for i,v in enumerate(lista):
    if v%2==0:
        pares.append(v)
    elif v%2==1:
        impar.append(v)
print(f'A lista informada foi {lista}')
print(f'Os numeros pares informados foram {pares}')
print(f'Os numeros impares informados foram {impar}')



