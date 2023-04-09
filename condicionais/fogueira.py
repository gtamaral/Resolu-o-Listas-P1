# variaveis 
nome_1 = input()
pontuação_1 = int(input())
nome_2 = input()
pontuação_2 = int(input())
nome_3 = input()
pontuação_3 = int(input())

# parte 01
if pontuação_1 > pontuação_2 and pontuação_2 > pontuação_3:
    print(f'{nome_3} {pontuação_3} \n{nome_2} {pontuação_2} \n{nome_1} {pontuação_1}')
elif pontuação_1 > pontuação_3 and pontuação_3 > pontuação_2:
    print(f'{nome_2} {pontuação_2} \n{nome_3} {pontuação_3} \n{nome_1} {pontuação_1}') 
elif pontuação_2 > pontuação_1 and pontuação_1 > pontuação_3:
    print(f'{nome_3} {pontuação_3} \n{nome_1} {pontuação_1} \n{nome_2} {pontuação_2}')
elif pontuação_2 > pontuação_3 and pontuação_3 > pontuação_1:
    print(f'{nome_1} {pontuação_1} \n{nome_3} {pontuação_3} \n{nome_2} {pontuação_2}')
elif pontuação_3 > pontuação_1 and pontuação_1 > pontuação_2:
    print(f'{nome_2} {pontuação_2} \n{nome_1} {pontuação_1} \n{nome_3} {pontuação_3}')
elif pontuação_3 > pontuação_2 and pontuação_2 > pontuação_1:
    print(f'{nome_1} {pontuação_1} \n{nome_2} {pontuação_2} \n{nome_3} {pontuação_3}')

# parte 02 => p1 == p2 == p3
elif pontuação_1 == pontuação_2 and pontuação_2 == pontuação_3:
    if nome_1 > nome_2 and nome_2 > nome_3:
        print(f'{nome_3} {pontuação_3} \n{nome_2} {pontuação_2} \n{nome_1} {pontuação_1}')
    elif nome_1 > nome_3 and nome_3 > nome_2:
        print(f'{nome_2} {pontuação_2} \n {nome_3} {pontuação_3} \n{nome_1} {pontuação_1}')
    elif nome_2 > nome_1 and nome_1 > nome_3:
        print(f'{nome_3} {pontuação_3} \n{nome_1} {pontuação_1} \n{nome_2} {pontuação_2}')
    elif nome_2 > nome_3 and nome_3 > nome_1:
        print(f'{nome_1} {pontuação_1} \n{nome_3} {pontuação_3} \n{nome_2} {pontuação_2}')
    elif nome_3 > nome_1 and nome_1 > nome_2:
        print(f'{nome_2} {pontuação_2} \n{nome_1} {pontuação_1} \n{nome_3} {pontuação_3}')
    elif nome_3 > nome_2 and nome_2 > nome_1:
        print(f'{nome_1} {pontuação_1} \n{nome_2} {pontuação_2} \n{nome_3} {pontuação_3}')

# parte 03 => 
elif pontuação_1 == pontuação_2 and pontuação_2 > pontuação_3:
    if nome_1 > nome_2:
        print(f'{nome_3} {pontuação_3} \n{nome_2} {pontuação_2} \n{nome_1} {pontuação_1}')
    elif nome_1 < nome_2:
        print(f'{nome_3} {pontuação_3} \n{nome_1} {pontuação_1} \n{nome_2} {pontuação_2}')

# parte 04
elif pontuação_1 == pontuação_2 and pontuação_2 < pontuação_3:
    if nome_1 > nome_2:
        print(f'{nome_2} {pontuação_2} \n{nome_1} {pontuação_1} \n{nome_3} {pontuação_3}')
    elif nome_1 < nome_2:
        print(f'{nome_1} {pontuação_1} \n{nome_2} {pontuação_2} \n{nome_3} {pontuação_3}')
    
# parte 05
elif pontuação_1 == pontuação_3 and pontuação_3 > pontuação_2:
    if nome_1 > nome_3:
        print(f'{nome_2} {pontuação_2} \n{nome_3} {pontuação_3} \n{nome_1} {pontuação_1}')
    elif nome_1 < nome_2:
        print(f'{nome_2} {pontuação_2} \n{nome_1} {pontuação_1} \n{nome_3} {pontuação_3}')

# parte 06
elif pontuação_1 == pontuação_3 and pontuação_3 < pontuação_2:
    if nome_1 > nome_3:
        print(f'{nome_3} {pontuação_3} \n{nome_1} {pontuação_1} \n{nome_2} {pontuação_2}')
    elif nome_1 < nome_3:
        print(f'{nome_1} {pontuação_1} \n{nome_3} {pontuação_3} \n{nome_2} {pontuação_2}')

# parte 07
elif pontuação_2 == pontuação_3 and pontuação_3 > pontuação_1:
    if nome_2 > nome_3:
        print(f'{nome_1} {pontuação_1} \n{nome_3} {pontuação_3} \n{nome_2} {pontuação_2}')
    elif nome_2 < nome_3:
        print(f'{nome_1} {pontuação_1} \n{nome_2} {pontuação_2} \n{nome_3} {pontuação_3}')
    
# parte 08 
elif pontuação_2 == pontuação_3 and pontuação_3 < pontuação_1:
    if nome_2 > nome_3:
        print(f'{nome_3} {pontuação_3} \n{nome_2} {pontuação_2} \n{nome_1} {pontuação_1}')
    elif nome_2 < nome_3:
        print(f'{nome_2} {pontuação_2} \n{nome_3} {pontuação_3} \n{nome_1} {pontuação_1}')

