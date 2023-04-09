# variaveis
nome_da_quadrilha = input()
passo_1 = input()
passo_2 = input()
passo_3 = input()
passo_4 = input()
passo_5 = input()
pontuação = float()
Casamento = False
escreveu_errado = False

# caso ocorra um passo nao listado ============================================
if passo_1 != 'Cumprimento' and passo_1 != 'Balancê' and passo_1 != 'Passeio' and passo_1 != 'Túnel' and passo_1 != 'Serrote' and passo_1 != 'Casamento' and passo_1 != 'Despedida':
   escreveu_errado = True
elif passo_2 != 'Cumprimento' and passo_2 != 'Balancê' and passo_2 != 'Passeio' and passo_2 != 'Túnel' and passo_2 != 'Serrote' and passo_2 != 'Casamento' and passo_2 != 'Despedida':
   escreveu_errado = True
elif passo_3 != 'Cumprimento' and passo_3 != 'Balancê' and passo_3 != 'Passeio' and passo_3 != 'Túnel' and passo_3 != 'Serrote' and passo_3 != 'Casamento' and passo_3 != 'Despedida':
    escreveu_errado = True
elif passo_4 != 'Cumprimento' and passo_4 != 'Balancê' and passo_4 != 'Passeio' and passo_4 != 'Túnel' and passo_4 != 'Serrote' and passo_4 != 'Casamento' and passo_4 != 'Despedida':
    escreveu_errado = True
elif passo_5 != 'Cumprimento' and passo_5 != 'Balancê' and passo_5 != 'Passeio' and passo_5 != 'Túnel' and passo_5 != 'Serrote' and passo_5 != 'Casamento' and passo_5 != 'Despedida':
    escreveu_errado = True

# variacoes dos passos ========================================================
# uso da pontuacao de acordo com o passo ======================================

#  passo 01
if passo_1 == 'Cumprimento':
    pontuação += 100 
elif passo_1 == 'Balancê':
    pontuação += 50
elif passo_1 == 'Passeio':
    pontuação += 70
elif passo_1 == 'Túnel':
    pontuação == pontuação * 0.9
elif passo_1 == 'Serrote':
    pontuação += 100
elif passo_1 == 'Casamento':
        Casamento = True
elif passo_1 == 'Despedida':
    pontuação += 0

# passo 02
if passo_2 == 'Cumprimento':
    pontuação += 10
elif passo_2 == 'Balancê':
    pontuação += 50
elif passo_2 == 'Passeio':
    pontuação += 70
elif passo_2 == 'Túnel':
    pontuação == pontuação * 0.9
elif passo_2 == 'Serrote':
    pontuação += 100
elif passo_2 == 'Casamento':
       Casamento = True
elif passo_2 == 'Despedida':
    pontuação += 0

# passo 03
if passo_3 == 'Cumprimento':
    pontuação += 10 
elif passo_3 == 'Balancê':
    pontuação += 50
elif passo_3 == 'Passeio':
    pontuação += 70
elif passo_3 == 'Túnel':
    pontuação == pontuação * 0.9
elif passo_3 == 'Serrote':
    pontuação += 100
elif passo_3 == 'Casamento':
      Casamento = True
elif passo_3 == 'Despedida':
    pontuação += 0

# passo 04
if passo_4 == 'Cumprimento':
    pontuação += 10 
elif passo_4 == 'Balancê':
    pontuação += 50
elif passo_4 == 'Passeio':
    pontuação += 70
elif passo_4 == 'Túnel':
    pontuação == pontuação * 0.9
elif passo_4 == 'Serrote':
    pontuação += 100
elif passo_4 == 'Casamento':
    Casamento = True
elif passo_4 == 'Despedida':
    pontuação += 0

# passo 05
if passo_5 == 'Cumprimento':
    pontuação += 10 
elif passo_5 == 'Balancê':
    pontuação += 50
elif passo_5 == 'Passeio':
    pontuação += 70
elif passo_5 == 'Túnel':
    pontuação == pontuação * 0.9
elif passo_5 == 'Serrote':
    pontuação += 100
elif passo_5 == 'Casamento':
    Casamento = True
elif passo_5 == 'Despedida':
    pontuação += 35

# validando o casamento
if Casamento == True:
    pontuação = pontuação * 2

# print do resultado
if escreveu_errado == True:
    print(f'Poxa, {nome_da_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')
else:
    print(f'Parabéns, {nome_da_quadrilha}! Bela apresentação. A pontuação foi de {pontuação}')

