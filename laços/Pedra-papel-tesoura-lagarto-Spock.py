N = int(input())
qntd_vitoria_sheldon = 0
qntd_vitoria_raj = 0

while N > 0:
    escolha_sheldon = input()
    escolha_raj  = input()
    N -= 1
    if escolha_sheldon == 'lagarto' and escolha_raj == 'spock':
        qntd_vitoria_sheldon += 1
    elif escolha_sheldon == 'spock' and escolha_raj == 'tesoura':
        qntd_vitoria_sheldon += 1
    elif escolha_sheldon == 'tesoura' and escolha_raj == 'lagarto':
        qntd_vitoria_sheldon += 1
    elif escolha_raj == 'lagarto' and escolha_sheldon == 'spock':
        qntd_vitoria_raj += 1
    elif escolha_raj == 'spock' and escolha_sheldon == 'tesoura':
        qntd_vitoria_raj += 1
    elif escolha_raj == 'tesoura' and escolha_sheldon == 'lagarto':
        qntd_vitoria_raj += 1
    elif escolha_raj == 'lagarto' and escolha_sheldon == 'lagarto' or escolha_raj == 'spock' and escolha_sheldon == 'spock' or escolha_raj == 'tesoura' and escolha_sheldon == 'tesoura':
        qntd_vitoria_sheldon += 0
        qntd_vitoria_raj += 0

if qntd_vitoria_raj > qntd_vitoria_sheldon:
    print('ENGOLE ESSA, SHELDON!')
elif qntd_vitoria_raj < qntd_vitoria_sheldon:
    print('BAZINGA! EU SOU O SENHOR DA SALA!')
else:
    print('Oh não, precisamos de outra rodada.')