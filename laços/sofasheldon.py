# variavies
ação = ''
Temperatura = 30
internet = 0
Fome = True
# comeco do while
while ação != 'parar':
        ação = input()
        if ação != 'ir para o grad' and ação != 'sair para a rua' and ação != 'comer uma quentinha' and ação != 'conectar no wifi' and ação != 'parar':
            print('Entrada inválida')
        elif ação == 'ir para o grad':
            Temperatura -= 5
            internet += 300
        elif ação == 'sair para a rua':
            Temperatura += 5
        elif ação == 'comer uma quentinha':
            Fome = False
        elif ação == 'conectar no wifi':
            internet += 100
       
# print das respostas
if (Temperatura >= 30):
    print('A temperatura aqui não está agradável')
elif (Temperatura <= 25):
    print('Agora sim, está aconchegante')

if Fome == True:
    print('Meu corpo precisa de comida')

if internet < 100:
    print('Essa conexão está horrível')

if Fome == False and Temperatura <= 25 and internet >= 300:
    print('Finalmente um lugar preciso para mim!')