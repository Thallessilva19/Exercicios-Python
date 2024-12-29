c=('\033[m,',
   '\033[0;30;41m',
   '\033[7;30m',
   '\033[0;30;44m'
   )


def python(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'',3)
    print([3])
    help(comando)
    print(c[0],end='')


def titulo(msg,cor=0):
    tam=len(msg)+4
    print(c[cor],end='')
    print('~'*tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')

user=''
while True:
    titulo( 'SISTEMA DE AJUDA PYHELP',1)
    user=str(input('Digite a função ou biblioteca:'))
    if user.upper()=='FIM':
        break
    else:
        python(user)
titulo('Até logo!',1)
