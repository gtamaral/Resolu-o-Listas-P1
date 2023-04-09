from re import I
# declarando a funcao das letras minusculas que recebe a lista
letra = ''
def letras_minusculas(lista_numeros):
    if lista_numeros(i) < 26:
        for i in range(0, 26):
            letra = chr(lista_numeros(i) + 15)
            return letra
    elif lista_numeros(i) >= 26 and lista_numeros(i) < 50:
        for i in (26, 50):
            letra = chr(lista_numeros(i) + 71)
            return letra

# declarando a funcao das letras maiusculas 
def letras_maiusculas(lista_numeros):
    if lista_numeros(i) >= 50 and lista_numeros(i) < 76:
        for i in range(50, 76):
            letra = chr(lista_numeros(i) + 15)
            return letra
    elif lista_numeros(i) > 75 and lista_numeros(i) < 100:
        for i in range(75, 100):
            letra = chr(lista_numeros(i) + 11)
            return letra

# iniciando o programa principal
# passo 01 => recebendo o input e separado os numeros pelo espaço entre eles.
# passo 02 => definindo uma variavel para a quantidade de numeros nessa lista.
lista_numeros = input().split(' ')
qntd_numeros = len(lista_numeros)

# invocando as funcoes 
for numero in range(qntd_numeros):
    
    if numero <= 26:
        letras_minusculas(lista_numeros)
    
    elif numero > 26 and numero < 50:
        letras_minusculas(lista_numeros)
    
    elif numero > 49 and numero < 76:
        letras_maiusculas(lista_numeros)

    elif numero > 75 and numero < 100:
        letras_maiusculas(lista_numeros)
    
    elif numero == 100:
        print(' ')
    


    
    

