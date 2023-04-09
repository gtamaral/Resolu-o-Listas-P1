# tamanho da matriz NxN
tamanho_matriz = int(input())
# declarando as listas e o max
maximo_linha = -999
maximo_coluna = -998
maximo_diagonal = -997
lista_matriz = []
lista_linha = []
lista_coluna = []
lista_diago = []

# transformando a matriz
for valor_eixo_x in range(tamanho_matriz):
    valor_eixo_x = input().split(' ')
    lista_matriz = []
    lista_matriz.append(valor_eixo_x)
# eixo x
for linha_index in range(tamanho_matriz):
    for coluna_index in range(tamanho_matriz - 1):
        valor_a = lista_matriz[linha_index][coluna_index]
        valor_b = lista_matriz[linha_index][coluna_index + 1]
        soma_linha = int(valor_a) + int(valor_b)
        if soma_linha > maximo_linha:
            maximo_linha = soma_linha
            indice_1 = valor_a + valor_b
# eixo y 
for linha_index in range(tamanho_matriz):
    for coluna_index in range(tamanho_matriz - 1):
        valor_c = lista_matriz[coluna_index][linha_index]
        valor_d = lista_matriz[coluna_index + 1][linha_index]
        soma_coluna = int(valor_c) + int(valor_d)
        if soma_coluna > maximo_coluna:
            maximo_coluna = soma_coluna
            indice_2 = valor_c + valor_d
# diagonal 
for linha_coluna_index in range(tamanho_matriz - 1):
    valor_e = lista_matriz[linha_coluna_index][linha_coluna_index]
    valor_f = lista_matriz[linha_coluna_index + 1][linha_coluna_index + 1]
    soma_diagonal = int(valor_e) + int(valor_f)
    if soma_diagonal > maximo_diagonal:
        maximo_diagonal = soma_diagonal
        indice_3 = valor_e + valor_f

# a senha 
senha = indice_1 + indice_2 + indice_3

# os prints
print(f'Falei que era fácil Dustinzinho...\nPegando todas os números que formam as combinações dos pares de cada sentido temos...\nPassword: {senha}')