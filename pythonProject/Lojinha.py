cont=0
menorvalor=0
soma=0
preco=0
p=0
barato=' '
while True:
    print('-'*30)
    print('LOJA')
    print('-' * 30)
    produto=str(input('Nome do produto:'))
    preco=float(input('Preço:R$'))
    soma += preco
    p+=1
    resp=' '
    if preco>1000:
        cont+=1
    if p==1:
        menorvalor=preco
        barato=produto
    else:
        if preco<menorvalor:
            menorvalor=preco
            barato=produto
    opcao=str(input('Quer continuar ? [S/N]')).upper()
    if opcao=='N':
        break
print(f'O total da compra foi {soma}')
print(f'Temos {cont} produto custando mais de 1000$')
print(f'O produto mais barato foi {barato} que custa RS{menorvalor:.2f}')

