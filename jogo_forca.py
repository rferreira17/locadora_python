import random
def jogar_forca():
    print('*'*35)
    print('*** Bem vindo ao jogo da Forca! ***')
    print('*'*35)
    palavras = []
    with open('palavras.txt') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero]

    letras_acertadas = ['_' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[posicao] = letra
                posicao = posicao + 1
        else:
            erros += 1
            print('Você errou! Tente novamente ainda tem {} tentativas\n'.format(5-erros))
        enforcou = erros == 5
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print('\n Parabéns, você ganhou!!')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.   .:|) |    ")
        print("      '-|:.   .:|- '    ")
        print("        \\::.   //      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print('\n Você perdeu')
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("      _______________         ")
        print("     /               \       ")
        print("    /                 \      ")
        print(" /\/                   \/\  ")
        print(" \ |   XXXX     XXXX   | /   ")
        print("  \|   XXXX     XXXX   |/     ")
        print("   |   XXX       XXX   |      ")
        print("   |                   |      ")
        print("   \__      XXX      __/     ")
        print("     |\     XXX     /|       ")
        print("     | |           | |        ")
        print("     | I I I I I I I |        ")
        print("     |  I I I I I I  |        ")
        print("     \_             _/       ")
        print("       \_         _/         ")
        print("         \_______/           \n")
        print('     Fim do jogo!!!')
