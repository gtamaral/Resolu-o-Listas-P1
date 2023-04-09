# primeiras entradas
dono_lista = input()
qntd_filmes = int(input())
# definindo as listas. obs. => separar depois a nota e o filme
lista_filme = []
lista_nota = []

# implementando a logica do bubble sort na lista. obs => colocar em ordem decrescente 
for i in range (qntd_filmes):
    string_filme = input()
    filme, nota = string_filme.split(' - ')

    lista_filme.append(filme)
    lista_nota.append(float(nota))
  
tamanholista = len(lista_nota) - 1
for i in range (tamanholista):
    for k in range (tamanholista):
        if lista_nota[k] > lista_nota[k + 1]:
            lista_nota[k],  lista_nota[k + 1] =  lista_nota[k + 1],  lista_nota[k]
            lista_filme[k], lista_filme[k + 1] = lista_filme[k + 1], lista_filme[k]
# print 
if dono_lista == 'Bonna':
    print('Os filmes sugeridos por Bonna são:')
else:
    print('Os filmes sugeridos por João são:')

for i in range(tamanholista):
    print(i)
    