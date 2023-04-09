# variaveis 
X = int(input())
Z = int(input())
# formulas
H2 = ((34-X)**2 + (220-Z)**2)
K2 = ((0-X)**2 + (0-Z)**2)
S2 = ((140-X)**2 + (456-Z)**2)
# calculo final 
H = float(H2**(1/2))
K = float(K2**(1/2))
S = float(S2**(1/2))
# resultado
print('Distancia para Hogsmeade: %.2f' %(H))
print('Distancia para Kakariko: %.2f' %(K))
print('Distancia para Solitude: %.2f' %(S))