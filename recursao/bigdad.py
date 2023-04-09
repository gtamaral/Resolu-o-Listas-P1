encerrou = False
encerrou_mestre = False
Bobby = {'grande_espada' : 8 , 'armadura_media' : 1}
Diana = {'dardo' : 12 , 'armadura leve' : 3}
Eric = {'grande_espada' : 8, 'armadura_pesada' : 0}
Hank = {'espada' : 6, 'armadura_media' : 1}
Presto = {'cajado' : 4, 'armadura_leve' : 3}
Sheila = {'espada' : 6, 'armadura_leve' : 3}
Uni = {'chifre' : 2, 'armadura_leve' : 3}
lista_grupo = [Bobby, Diana, Eric, Hank, Presto, Sheila, Uni]

adversario = {'Vingador' : 30 , 'Tiamat' : 20 , 'Vingador das Sombras' : 14 , 'Outro' : 9}

nome_adversario = input()
if nome_adversario != 'Vingador' and nome_adversario != 'Tiamat' and nome_adversario != 'Vingador das Sombras':
    vida_adversario = 9
else:
    vida_adversario = adversario[nome_adversario]

turnos = int(input())

while encerrou == False and encerrou_mestre == False:
    nome_personagem = input()
    
    if nome_personagem == 'Bobby':
        vida_adversario = vida_adversario - Bobby['grande_espada']
        turnos = turnos - (1 + Bobby['armadura_media'])
    elif nome_personagem == 'Diana':
        vida_adversario = vida_adversario - Diana['dardo']
        turnos = turnos - (1 + Diana['armadura leve'])
    elif nome_personagem == 'Eric':
        vida_adversario = vida_adversario - Eric['grande_espada']
        turnos = turnos - (1 + Eric['armadura_pesada'])
    elif nome_personagem == 'Hank':
        vida_adversario = vida_adversario - Hank['espada']
        turnos = turnos - (1 + Hank['armadura_media'])
    elif nome_personagem == 'Presto':
        vida_adversario = vida_adversario  - Presto['cajado']
        turnos = turnos - (1 + Presto['armadura_leve'])
    elif nome_personagem == 'Sheila':
        vida_adversario = vida_adversario - Sheila['espada']
        turnos = turnos - (1 + Sheila['armadura_leve'])
    elif nome_personagem == 'Uni':
        vida_adversario = vida_adversario - Uni['chifre']
        turnos = turnos - (1 + Uni['armadura_leve'])
       
       
    if vida_adversario <= 0 or turnos <= 0:
        encerrou = True
    if nome_personagem == 'Mestre dos Magos':
        encerrou_mestre = True

if encerrou == True:
    if vida_adversario <= 0:
        print (f'{nome_personagem} executou o ultimo golpe em {nome_adversario}, estamos livres!')
    else:
        print (f'Oh nao, {nome_adversario} e muito forte, este e o fim!')

if encerrou_mestre == True:
    print ('Muito obrigado amigo, que nos vejamos novamente um dia')        

