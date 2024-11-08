m=0
mulhermenor=0
maior18=0
while True:
    print('Cadastre uma pessoa')
    print('-'*20)
    idade=int(input('Idade:'))
    if idade>=18:
        maior18+=1
    sexo=str(input('[M/F]?')).upper()
    if sexo=='M':
        m+=1
    elif sexo=='F':
        if idade<=19:
          mulhermenor+=1
    opção=str(input('Quer continuar? [S/N]')).upper().strip()
    if opção=='N':
        break
print(f'foram informadas {maior18} pessoas maiores de idade')
print(f'Foram informados {m} pessoas do sexo masculino')
print(f'foram informados {mulhermenor}mulheres menores de 20 anos')