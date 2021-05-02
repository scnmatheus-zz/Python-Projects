print('===================NETinfo informática e telecomunicações===================')
nome = input("Seja muito bem vindo ao sistema NETinfo, por favor diga-me seu nome ;) :")
notaum = float(input(f'Olá, {nome}, tudo bem com você? esperamos que sim! diga-me qual sua nota de matemática? : '))
notadois = float(input(f'Certo, {nome}! agora para finalizarmos, diga-me qual sua nota de português, por favor? : '))
med = (notaum + notadois) /2

print(f'Sua nota em matemática foi {notaum} e sua nota em português foi {notadois} portanto, \n sua média nesse semestre foi {med}')