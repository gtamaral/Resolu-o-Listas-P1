# definindo a funcao recursiva 
# obs == rascunho (ainda nao sei como usar a funcao recursiva nessa questao) == apenas uma ideia, mas achei mais 
# (continuacao) conveniente usar esses casos fora da funcao
from optparse import check_choice


def check_caracter(current, caracter):
        # caso base => 
        if current == ' ':
            return 0
        # caso recursivo
        else:
            if current[0] == caracter: 
                return 1 + check_caracter(current[1:], caracter)
            else:
                return 0 + check_caracter(current[1:], caracter)
                
 
# first i put => recebendo a qntd de operacoes e criando um for pra adiciar essas operacoes em uma lista
qntd_op =int(input())
equacoes = []
for i in range(qntd_op):
    equacoes.append(input())

# criar um for p/ analisar cada elemento dessa lista 
for eq in equacoes:
    # criando variavel para checar os "(' ')"
    # usando o .count para saber quantos de cada um eu vou ter 
    right = check_caracter(eq, '(')
    left = check_caracter(eq, ')')


    # criando comandos para analisar a qntd de 'right' e 'left'
    if right == left:
        print('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif right > left:
        print('A quantidade de parênteses \'(\' está maior que a de \')\', vamos descartá-la')
    else:
        print('A quantidade de parênteses \')\' está maior que a de \'(\', vamos descartá-la')
    