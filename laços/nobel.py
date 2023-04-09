  # variaveis 

mensagem_N = ''
sheldon_acabou = False
pontuacao = 0
xingamento = False
bazinga = False
feito_1 = 'Começou a Trabalhar na Caltech'
feito_2 = 'Trabalho sobre a String Theory'
feito_3 = 'Ganhar o Chancellor de ciência'
feito_4 = 'Pensar na Teoria de Cooper-Hofstader'
feito_5 = 'Criou a Super Assimetria'
feito_6 = 'Ganhar o Nobel'
  # comeco do while
while sheldon_acabou == False:
    mensagem_N = input()
  #feito1
    if pontuacao == 0 and mensagem_N == feito_1:
        pontuacao += 1 
        xingamento = False
        bazinga = False
          
  #xingamento
    elif mensagem_N == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or mensagem_N == 'Leonard seu anão covarde' or mensagem_N == 'Tu é muito burro Raj':
        print('Não xingue seus amigos Sheldon!')
        bazinga = True
    
  #se acabar e pontuacao = 6 
    elif mensagem_N == 'É o fim da Estrada pra Sheldon Cooper' or  pontuacao == 6 :
        sheldon_acabou = True
  # bazinga's  
   
    elif mensagem_N == 'Bazinga'and bazinga == False:
      pontuacao -= 1
      bazinga = True
    
    else:
        bazinga = True
  
  # feito 2 
    if pontuacao == 1:
      if mensagem_N == feito_2:
          pontuacao += 1
          xingamento = False
          bazinga = False

      if mensagem_N == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
        sheldon_acabou = True
  # feito 3  
    if pontuacao == 2:
      if mensagem_N == feito_3:
          pontuacao += 1
          xingamento = False
          bazinga = False

      if mensagem_N == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
        sheldon_acabou = True
  # feito 4
    if pontuacao == 3:
      if mensagem_N == feito_4:
          pontuacao += 1
          xingamento = False
          bazinga = False

    if mensagem_N == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
        sheldon_acabou = True
  # feito 5
    if pontuacao == 4:
      if mensagem_N == feito_5:
          pontuacao += 1 
          xingamento = False
          bazinga = False

      if mensagem_N == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
        sheldon_acabou = True
  # feito 6    
    if pontuacao == 5:
      if mensagem_N == feito_6:
          pontuacao += 1 
          xingamento = False
          bazinga = False
          sheldon_acabou = True
      
      if mensagem_N == 'É o fim da Estrada pra Sheldon Cooper' or pontuacao == 6:
        sheldon_acabou = True

    
  # final
if sheldon_acabou == True:
    if pontuacao == 0:
        print('Que potencial desperdiçado...')
    elif pontuacao == 1:
        print('Tão perto, mas tão longe')
    elif pontuacao == 2:
        print('Tão perto, mas tão longe')
    elif pontuacao == 3:
        print('Não desista Sheldon, você ainda têm muito para alcançar!')
    elif pontuacao == 4:
        print('Não desista Sheldon, você ainda têm muito para alcançar!')
    elif pontuacao == 5:
        print('Nãoooooo, esse momento ia ser seu Sheldon')
    elif pontuacao == 6:
        print('Você conseguiu Sheldon, o Nobel é seu!!!')
        