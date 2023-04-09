# recebendo os primeiros inputs
A = int(input())
L = int(input())
P = int(input())
H = int(input())

# iniciando as contas
X = (A+L + abs(A-L)) / 2
Y = int((X+P + abs(X-P)) /2)
M = int(H*Y)

# printando o resultado
print(M)
