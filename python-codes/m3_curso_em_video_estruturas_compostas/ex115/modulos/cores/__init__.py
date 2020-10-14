def colorizar(texto_para_colorir,cor_escolhida):
    if cor_escolhida == 'amarelo':
        texto_para_colorir = f'\033[0;33m{texto_para_colorir}\033[m'