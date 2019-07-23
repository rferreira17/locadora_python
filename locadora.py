import jogo_adivinhacao
import jogo_forca
import palavras

print('*'*35)
print('******** Locadora do Cobra ********')
print('*'*35)

print('Escolha seu jogo')
print('(l) Jogo da Adivinhação\n(2) Jogo da Forca\n')

jogo = int(input('Defina o Jogo que quer jogar: '))

if (jogo == 1):
    print('Jogando Adivinhação')
    jogo_adivinhacao.jogar_adivinhacao()
elif (jogo == 2):
    print('(l) Para jogar jogo da Forca\n(2) Para cadastrar palavras')
    option = int(input('Escolha uma opção: '))
    if(option == 1):
        jogo_forca.jogar_forca()
    elif(option == 2):
        print('Salvar palavras')
        palavras.palavras()
