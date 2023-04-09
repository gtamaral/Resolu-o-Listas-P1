# recebendo os inputs
C1 = input()
# tratando a nota como float pela forma que ela vem
N1 = float(input())
# e a distancia como input
D1 = int(input())
C2 = input()
N2 = float(input())
D2 = int(input())
C3 = input()
N3 = float(input())
D3 = int(input())

# comeco da logica ------------------------------------------------- e printando o resulado
if N1 < 4 and N2 < 4 and N3 < 4:
    print("Nota mínima não atingida")
elif N1 == N2 and N2 == N3:
    if D1 < D2 and D1 < D3:
        print(C1)
    elif D2 < D3:
        print(C2)
    else:
        print(C3)
else:
    if N1 > N2 and N1 > N3:
        print(C1)
    elif N2 > N3:
        print(C2)
    else:
        print(C3)
        