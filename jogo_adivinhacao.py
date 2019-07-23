from random import randint
def jogar_adivinhacao():
    print('*'*30)
    print('**** Jogo da Adivinhação ****')
    print('*'*30)

    rodada = 1
    nivel = int(input('Digite o nível do jogo:\n1 - Fácil \n2 - Médio \n3 - Difícil\n'))
    if nivel == 1:
        tentativas = 3
        numero = randint(0,10)
        print('Digite um número de O até 10')

    elif nivel  == 2:
        tentativas = 10
        numero = randint(0,30)
        print('Digite um número de O até 50')
    elif nivel == 3:
        tentativas = 20
        numero = randint(0,100)
        print('Digite um número de O até 100')


    while rodada <= tentativas:
        print('Tentativa {}, de {} possíveis,'.format(rodada,  tentativas))
        chute = int(input('Digite um número: '))
        print('Você digitou: ', chute)

        acertou = chute == numero
        maior = chute > numero
        menor = chute < numero
        if acertou:
            print('Você acertou! Se garantiu.')
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
            break
        elif maior:
            print('Você errou! Você digitou um numero maior')
        elif menor:
            print('Você errou! Você digitou um numero menor')

        rodada = rodada + 1

    print('Game  Over')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('O número premiado é ',numero)
    print('Suas tentativas foram: ', chute)
