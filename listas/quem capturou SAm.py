# ATUALIZANDO CODE 11/08

# lista de suspeitos
lista_suspeito = input().split(',')
# checando as entradas
while len(lista_suspeito) != 1:
    entrada = input()
    if entrada == 'Não encontrei nada no primeiro suspeito':
        lista_suspeito.pop(0)
    elif entrada == 'O último da lista está limpo':
        lista_suspeito.pop()
    # o caso do elemento do meio (n sei como tirar o indice do meio)
    elif entrada == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita':
      centro = len(lista_suspeito) // 2
      lista_suspeito.pop(centro)
    #   input da posicao pra eliminar
    elif entrada == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:':
      posicao_suspeito = int(input())
      lista_suspeito.pop(posicao_suspeito)
    
    # input com novo suspeito
    elif entrada == 'Acho que temos mais uma opção a ser analisada…':
      nome_suspeito = ()
      lista_suspeito.append(nome_suspeito)
    else:
      print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')
# quando sobre apenas um suspeito
else:
    suspeito_final = lista_suspeito[0]
    print(f'Acho que encontramos o suspeito. O seu nome é {suspeito_final}, vamos salvar o Sam!')






