reação_boa = 0
reação_ruim = 0
total_reacoes = float()
piada_N = str()

# para uma piada ser bastante suérior a outra, ela deve ter mais de 60% do total de reacao. Se nao, é equilibrio
while piada_N != 'Fim do Show!':
    piada_N = input()
    if piada_N != 'Fim do Show!':
        reação_N = input()
        if reação_N == 'BAZINGA!':
            reação_boa += 1
            total_reacoes  += 1
        elif reação_N != 'BAZINGA!':
            reação_ruim += 1
            total_reacoes += 1

if reação_boa == total_reacoes * 0.6:
    print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif reação_ruim == total_reacoes * 0.6:
    print('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')
else:
    print('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')
