

lista=[]
maior=0
menor=0
for cont in range(1,6):
    lista.append(int(input(f'Digite um valor para a posição {cont}:')))
    if cont==1:
        maior=menor=[cont]
    else:
        if [cont]>maior:
            maior=[cont]
        if [cont]<menor:
            menor=[cont]
print(f'Você digitou os valores {lista}')
print(f'O maior valor informado foi {max(lista)} e está na posição {maior} ',end=' ')
print(f'O menor valor da lista foi {min(lista)} e está na posição {menor}')