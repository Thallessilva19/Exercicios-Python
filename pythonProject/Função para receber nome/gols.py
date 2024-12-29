def ficha(nome='Desconhecido',gols=0):
    if not isinstance(gols,int):
        gols=0
    return (f'O jogador {nome} fez {gols} ')


jogador=str(input('Nome do jogador:'))
gols=(input('Numero de gols:'))
print(ficha(jogador,gols))
