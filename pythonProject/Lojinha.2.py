

print('''=======LOJA DO THALLES========''')
preco=float(input('Qual o preço das compras:R$'))
print('''FORMAS DE PAGAMENTO
[1] Á vista dinheiro ou cheque
[2]Á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
forma=int(input('Qual a forma de pagamento?'))
if forma==1:
    total=preco-(preco*10/100)

elif forma==2:
    total=preco-(preco*5/100)
elif forma==3:
    total=preco
    parcela=preco/2
    print('Sua compra será parcelada em duas vezes de {:.2f}'.format(total))
elif forma==4:
    total=preco+(preco*20/100)
    top=int(input('Em quantas parcelas será a compra?'))
    parcela=total/top
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(top,parcela))
else:
    total=0
    forma!=1!=2!=3!=4
    print('Opção invalida,Escolha uma das opções acima')

print('Sua compra de R${:.2f} irá custar RS{:.2f}'.format(preco,total))



