def notas(*n,sit=False):
    """
    :param n:Uma ou mais notas dos alunos
    :param sit:Valor opcional indicando se dever ou não indicar situação da turma
    :return:Dicionário com varias informações sobre a turma
    """
    r={}
    r['Total']=len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    r['media']=sum(n)/len(n)
    if r['media']>=7:
        r['situação']='Boa'
    elif r['media']>=5:
        r['situação']='Razoavel'
    else:
        r['situação']='RUIM'
    return r


resp=notas(5.5, 2.5,7,sit=True)
print(resp)