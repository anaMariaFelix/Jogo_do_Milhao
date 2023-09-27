from random import choice,shuffle,randint
from arquivo import ler_arquivo

tamanho_carac = 50

nivel_01 = []
nivel_02 = []
nivel_03 = []
nivel_04 = []
nivel_05 = []

caminho_arquivo = '../arquivo_perguntas.txt'

def preenche_niveis():
    perguntas_no_arquivo = ler_arquivo(caminho_arquivo)
    for linha in perguntas_no_arquivo[:12]:
        pergunta = linha.split('_')
        pergunta[4] = pergunta[4].rstrip('\n')
        nivel_01.append(pergunta)

    for linha in perguntas_no_arquivo[13:24]:
        pergunta = linha.split('_')
        pergunta[4] = pergunta[4].rstrip('\n')
        nivel_02.append(pergunta)

    for linha in perguntas_no_arquivo[25:36]:
        pergunta = linha.split('_')
        pergunta[4] = pergunta[4].rstrip('\n')
        nivel_03.append(pergunta)

    for linha in perguntas_no_arquivo[37:48]:
        pergunta = linha.split('_')
        pergunta[4] = pergunta[4].rstrip('\n')
        nivel_04.append(pergunta)

    for linha in perguntas_no_arquivo[49:60]:
        pergunta = linha.split('_')
        pergunta[4] = pergunta[4].rstrip('\n')
        nivel_05.append(pergunta)


letras_das_alternativas = ['(A)','(B)','(C)','(D)']


def redefinir_lista_letra_das_alternativas():
    global letras_das_alternativas
    letras_das_alternativas.clear()
    letras_das_alternativas.append('(A)')
    letras_das_alternativas.append('(B)')
    letras_das_alternativas.append('(C)')
    letras_das_alternativas.append('(D)')

def remove_alternativa(pergunta_sorteada):

    letras_das_alternativas.pop(randint(0,3))
    letras_das_alternativas.pop(randint(0,2))

    pergunta_sorteada.remove(pergunta_sorteada[randint(2,4)])
    pergunta_sorteada.remove(pergunta_sorteada[randint(2,3)])

    return pergunta_sorteada


def validador_resposta_da_alternativa(resposta_da_alternativa_escolhida,pergunta_sorteada):
    if resposta_da_alternativa_escolhida == pergunta_sorteada[1]:
        return True
    else:
        return False


def procurando_indice_da_alternativa_esolhida(escolha_alternativa,embaralho):
    indice_da_alternativa_esolhida = letras_das_alternativas.index(escolha_alternativa)
    pega_resposta_da_alternativa_escolhida = embaralho[indice_da_alternativa_esolhida]
    return pega_resposta_da_alternativa_escolhida


def embaralhando_alternativas(pergunta):
    embaralho = pergunta[1:]
    shuffle(embaralho)
    return embaralho


def sorteia_pergunta(quant_acertos):
    if quant_acertos == 0:
        pergunta = choice(nivel_01)
        nivel_01.remove(pergunta)
        return pergunta

    elif quant_acertos == 1:
        pergunta = choice(nivel_02)
        nivel_02.remove(pergunta)
        return pergunta

    elif quant_acertos == 2:
        pergunta = choice(nivel_03)
        nivel_03.remove(pergunta)
        return pergunta

    elif quant_acertos == 3:
        pergunta = choice(nivel_04)
        nivel_04.remove(pergunta)
        return pergunta

    elif quant_acertos == 4:
        pergunta = choice(nivel_05)
        nivel_05.remove(pergunta)
        return pergunta





