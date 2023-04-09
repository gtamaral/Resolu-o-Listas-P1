Pokedex = {}
acabou = False

while acabou == False:
    
    try:  
        pokemon = input().split()
        
        if pokemon[0] == 'ADD' :            
            if pokemon[1] in Pokedex.keys():            
                print ('Pokémon já adicionado na Pokédex')
            else:
                entrada_desc = input()
                Pokedex.update({pokemon[1] : entrada_desc})
                print ('Pokémon adicionado com sucesso')

        elif pokemon[0] == 'DESC' :
            if pokemon[1] in Pokedex.keys():
                print (Pokedex[pokemon[1]])
            else:
                print ('Ainda não há registro desse Pokémon')

    except:
        acabou = True
        break 
        