import numpy

palavra = ['bolacha''boliche', 'abacaxi', 'framboesa', 'carta', 'baralho', 'carro', 'colher','paralelepipedo','coelho','bicicleta']
elemento = numpy.random.choice(palavra)
secreto = elemento
str(secreto)
chance = 6
digitadas = []
print('Jogo da forca')
print(f"A palavra escolhida tem {len(secreto)} letras ")
while True:
    letra = str(input(f'Digite uma letra.\nVoce tem {chance} chances')).lower()
    if 1 < len(letra):
        print(f'Digite apenas uma letra voce tem {chance} chances')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'Voce acertou!!!!!')
    else:
        chance -= 1
        print(f'Voce errou a letra "{letra}" não existe na palavra voce tem {chance}')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)
    if secreto_temporario == secreto:
        print(f'Parabens voce ganhou!!!.\nA palavra secreta é {secreto} Voce usou {chance} chances')
        break
    elif chance ==0:
        print(f'Voce perdeu!!!.\nA palavra secreta era {secreto}.')
        break
