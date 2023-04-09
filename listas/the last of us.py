
# declarando as primeiras variaveis ( quantidade mochila)
from operator import index


qntd_mochilas = int(input())
# as listas => donos e big lista ( mochilas com itens)
donos = input().split(' ')
lista_mochilas = [0] * qntd_mochilas
encerrou = False

# definindo os itens iniciais dentro do indice de cada mochila
for i in range(qntd_mochilas):
    tamanho_mochila = int(input())
    lista_mochilas[i] = [0] * tamanho_mochila
    lista_mochilas[i][0] = 'Lanterna' 
    lista_mochilas[i][1] = 'Omega 3 da top therm'

   # tamanho_mochila[i] >= 2

# duvida sobre o input das qntd_itens e itens
# obs => lista_mochilas[indice_incessao] == alguma mochila 
qntds_itens_adicionar = int(input())
for i in range(qntds_itens_adicionar):
    item = input()
    indice_incessao = int(input())
    if 0 in lista_mochilas[indice_incessao]:
        index_0 = lista_mochilas[indice_incessao].index(0)
        lista_mochilas[indice_incessao][index_0] = item
    else:
        print('Mochila cheia. Não vai dar para levar.')


# comeco do while
# ajeitar as variaveis do espaco disponivel e qntds
while encerrou == False:
    entrada = input()

# as entradas   
    if entrada == 'Tirar da mochila':
       novo_item = input()
       indice_incessao = int(input())
       if novo_item == lista_mochilas[indice_incessao]:
        index_novo_item = lista_mochilas[indice_incessao].index(novo_item)
        lista_mochilas[indice_incessao][index_novo_item] = 0
        print(f'{novo_item} usado com sucesso da mochila{indice_incessao}.')
       else:
        print(f'Você não tem {novo_item} na {indice_incessao}.')
    # entrada pra adicionar na mochila   
    elif entrada == 'Guardar na mochila':
        novo_item = input()
        indice_incessao = int(input())
        if 0 in lista_mochilas[indice_incessao]:
            index_0 = lista_mochilas[indice_incessao].index(0)
            lista_mochilas[indice_incessao][index_0] = novo_item
            print(f'{novo_item} adicionado na mochila {indice_incessao}.')
        else:
            print(f'Mochila {indice_incessao} cheia!')
  # entrada pra encerrar       
    elif entrada == 'CHEGAMOS NO CIN!':  
        encerrou = True
        break
# entradas invalidas
    else:
        print('Ação inválida.')
# the last print: com a quantidade de amigos
qntd_friends = len(donos) 
for i in range (qntd_friends):
    qntd_itens_i = len(lista_mochilas[i])
    print(f' Mochila de {donos[i]} chegou assim: ')
    for j in range (qntd_itens_i):
        if (lista_mochilas[i][j]) != 0:
            print(lista_mochilas[i][j])

