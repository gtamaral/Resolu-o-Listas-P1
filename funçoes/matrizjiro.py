# passo 01 
# definindo todas as funcoes pro resto do codigo

def soma_matriz(m1, m2):
    resultado = []
    for i in range(len(m1)):
        resultado.append([])
        for j in range(len(m1[0])):
            resultado[i].append(m1[i][j] + m2[i][j])
    return resultado


def sub_matriz(m1, m2):
    resultado = []
    for i in range(len(m1)):
        resultado.append([])
        for j in range(len(m1[0])):
            resultado[i].append(m1[i][j] - m2[i][j])
    return resultado

# multiplicacao NORMAL
def multiplicationMatrices(m1, m2):
    def getLinha(matriz, n):
        return [i for i in matriz[n]]  # ou simplesmente return matriz[n]

    def getColuna(matriz, n):
        return [i[n] for i in matriz]

    mat1lin = len(m1)
    mat2col = len(m2[0])

    matRes = []
    for i in range(mat1lin):
        matRes.append([])
        for j in range(mat2col):
            listMult = [x * y for x, y in zip(getLinha(m1, i), getColuna(m2, j))]
            matRes[i].append(sum(listMult))

    return matRes

#  multiplicacao ESCALAR
def multiplicationScalar(matrix, k):
    resultado = []
    for line in matrix:
        resultado.append([elem * k for elem in line])
    return resultado


#  recebendo o input q defini o tam das duas matrizes
N = int(input())

#  criando a matriz
M1 = []
for index in range(N):
    line = input().split(' ')
    M1.append([int(i) for i in line])

M2 = []
for index in range(N):
    line = input().split(' ')
    M2.append([int(i) for i in line])

# quantidade de operacoes
qtd_op = int(input())

# iniciando as operacoes
operacoes = []
for index in range(qtd_op):
    line = input().split(' ')
    operacoes.append(line)

resultado = []
for operacoes in operacoes:
    if operacoes[0] == 'm1' and '*' not in operacoes:
        Ma = None
        if operacoes[2] == 'm1':
            Ma = M1
        else:
            Ma = M2
        Mb = None
        if operacoes[4] == 'm1':
            Mb = M1
        else:
            Mb = M2
        # print(Ma)
        # print(Mb)
        if operacoes[3] == '+':
            resultado = soma_matriz(Ma, Mb)
            M1 = resultado
        elif operacoes[3] == '-':
            resultado = sub_matriz(Ma, Mb)
            M1 = resultado
        elif operacoes[3] == '.':
            resultado = multiplicationMatrices(Ma, Mb)
            M1 = resultado
    elif operacoes[0] == 'm1' and '*' in operacoes:
        A = None
        B = None
        if operacoes[2] == 'm1' or operacoes[2] == 'm2':
            if operacoes[2] == 'm1':
                A = M1
            else:
                A = M2
            B = int(operacoes[4])
        else:
            B = int(operacoes[2])
            if operacoes[4] == 'm1':
                A = M1
            else:
                A = M2
        resultado = multiplicationScalar(A, B)
        M1 = resultado
    elif operacoes[0] == 'm2' and '*' not in operacoes:
        Ma = None
        if operacoes[2] == 'm1':
            Ma = M1
        else:
            Ma = M2
        Mb = None
        if operacoes[4] == 'm1':
            Mb = M1
        else:
            Mb = M2
        if operacoes[3] == '+':
            resultado = soma_matriz(Ma, Mb)
            M2 = resultado
        elif operacoes[3] == '-':
            resultado = sub_matriz(Ma, Mb)
            M2 = resultado
        elif operacoes[3] == '.':
            resultado = multiplicationMatrices(Ma, Mb)
            M2 = resultado
    elif operacoes[0] == 'm2' and '*' in operacoes:
        A = None
        B = None
        if operacoes[2] == 'm1' or operacoes[2] == 'm2':
            if operacoes[2] == 'm1':
                A = M1
            else:
                A = M2
            B = int(operacoes[4])
        else:
            B = int(operacoes[2])
            if operacoes[4] == 'm1':
                A = M1
            else:
                A = M2
        resultado = multiplicationScalar(A, B)
        M2 = resultado

# the last part: o print
for line in resultado:
    s = ' '
    cLine = [str(i) for i in line]
    print(s.join(cLine))