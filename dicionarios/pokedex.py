# você deve criar um algoritmo, que recebe um numero indefinido de entradas
# com os comandos 'ADD' ou 'DESC'

# pokedex = lista para arnazenar os dicionarios
# entrada, uma lista para armazenar cada pokemon e seus 


pokedex = []
dados = {}
# a entrada basicamente comeca com um comando ( ADD OU DESC), em seguida o o nome do pokemon e por fim
# a descricao do pokemnon ///////// ideia => armazenar a entrada em uma lista e verificar cada elemento 
while True:
    try: 
        dados['comando'] = str(input())
        dados['nome'] = str(input())
        dados['desc'] = str(input())
        pokedex.append(dados)
        # condicao para se a entrada pedir a desc do pokemon
        if dados['comando'] == 'DESC':
            if dados['nome'] in pokedex:
                if dados['nome'] == 'Charmander':
                    print ('A chama em sua cauda indica a força vital de Charmander, se estiver saudável, a chama queima brilhantemente.')
                elif dados['nome'] == 'Bulbassauro':
                    print('A semente em suas costas é cheia de nutrientes. A semente fica cada vez maior à medida que seu corpo cresce.')
                elif dados['nome'] == 'Squirtle':
                    print('Quando retrai seu longo pescoço em sua concha, esguicha água com força vigorosa.')
            else:
                print('Ainda não há registro desse Pokémom')
        # condicao para a entrada ADD do pokemon
        if dados['comando'] == 'ADD':
            if dados['nome'] not in pokedex:
                pokedex.append(dados)
                print('Pokémon adicionado com sucesso')
            else:
                print('Pokémon já adicionado na Pokédex')
    except EOFError:
        break



