def ler_arquivo(caminho):
    try:
        abri = open(caminho, 'rt', encoding='utf8')
        perguntas_arquivadas = abri.readlines()
        abri.close()
        return perguntas_arquivadas

    except:
        print('Não foi possivel abrir o arquivo')

