score = 0
n = 0
n1 = 0
quantidade_arremessos = int(input())
lista1 = input().split()
lista2 = input().split()
dicionario_score = {}

try:
    while n != (quantidade_arremessos**2) and n1 != (quantidade_arremessos):
        if lista1[n] in lista2[n1]:
            score = score + 1
            n = n + 1
            lista2.pop(n1)    
            n1 = 0
        else:
            n1 = n1 + 1

except:
    if score == quantidade_arremessos:
        dicionario_score = {'resultado' : 'empate'}
    else:
        dicionario_score = {'resultado' : 'derrota'}

    if dicionario_score['resultado'] == 'empate':
        print ('Dale Gohan!')    
    else:
        print ('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')           



