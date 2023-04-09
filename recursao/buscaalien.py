#  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#  Lógica da questao => 1. receber uma lista com as salas 2. o numero escolhido 3. qnt de bits que o robo vai suportar
#  (cont) => depois de receber os inputs, criar uma funcao rec de busca binaria para achar o number chosen
# (cont) => depois criar uma funcao para transformar o numero decimal para bits

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

#  definindo a funcao pra transformar o resultado em binario
def decimal_for_bits(number_chosen):
    resto = number_chosen % 2
    number_chosen = number_chosen // 2
    lista_binaria.append[resto]

    # caso base
    if number_chosen == 0:
        return 0
    # caso recursivo 
    else:
        if number_chosen != 0:
            return decimal_for_bits(number_chosen)

lista_binaria = []
# invertendo a lista
lista_binaria = lista_binaria[::-1]

# def a funcao recursiva para busca binaria
def search_binary(rooms_numbers_int, esquerda, direita, number_chosen):
    # caso base  = o elemento nao esta presente
    meio = (esquerda + direita) // 2
    if direita < esquerda:
        return 0
    # caso recursivo == chamando a propria funcao
    else:
        if rooms_numbers[meio] == number_chosen:
            lista_caminho.append['meio']
            return meio
        elif rooms_numbers[meio] > number_chosen:
            lista_caminho.append['esquerda']
            return search_binary(rooms_numbers_int, esquerda, meio -1, number_chosen)
        else:
            lista_caminho.append['direita']
            return search_binary(rooms_numbers_int, meio + 1, direita, number_chosen)


# first input => recebendo a lista com a numeracao das salas
rooms_numbers = input().split(' ')

# transformado a lista com os numeros para int p/ facilitar nas comparacoes
rooms_numbers_int = []
for i in rooms_numbers:
    i = int()
    rooms_numbers_int.append(i)

# numero escolhido
number_chosen = int(input())
# quantidade de bits
qnt_bits = int(input())

# lista para os caminhos 
lista_caminho = []

# output
#  iniciando com o if para quando o numero escolhido estiver na lista e iniciando os subcasos
while len(lista_binaria) > 0:
    
    if number_chosen in lista_binaria:
        if len(lista_binaria) <= qnt_bits:
            print(f'{lista_caminho}, seguindo por essas coordenadas você vai chegar no número {lista_binaria}')

        elif len(lista_binaria ) > qnt_bits:
             print('Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.')
# iniciando agora para quando o numero nao tiver na lista 
    else:
        if number_chosen < rooms_numbers_int[0] and number_chosen > rooms_numbers_int[-1]:
             print('Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.')
        elif number_chosen > rooms_numbers_int[0] and number_chosen < rooms_numbers_int[-1]:
            print(f'{lista_caminho}, mas não consegui achar.')
        else:
             print('Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.')    
    