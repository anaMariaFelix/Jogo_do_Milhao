from logica import *

valor_do_premio = 1000
quant_acertos = 0
quant_pulos = 0
quant_vezes_que_pode_pedir_ajuda = 0


def imprime_certa_resposta():
    print()
    print('--'*21, 'CERTA RESPOSTA', '--'*21)
    print('--' * tamanho_carac)
    print()
    print('Nova pergunta:')
    print('--' * tamanho_carac)
    sorteado_de_novas_perguntas()


def contabiliza_resultado():
    global quant_acertos,valor_do_premio
    quant_acertos += 1
    if quant_acertos <= 2:
        valor_do_premio *= 10
        imprime_certa_resposta()

    elif quant_acertos == 3:
        valor_do_premio = valor_do_premio * 5
        imprime_certa_resposta()

    elif quant_acertos == 4:
        valor_do_premio = valor_do_premio * 2
        imprime_certa_resposta()

    elif quant_acertos == 5:
        print('--' * tamanho_carac)
        print('--'*21, 'CERTA RESPOSTA', '--'*21)
        print()
        print(f'Você acabou de ganhar R${valor_do_premio:,.2f}')
        print()
        print('--' * tamanho_carac)
        print()
        tela_inicial()


def reficador_da_resposta(resultado_da_resposta):
    if resultado_da_resposta == True:
        if quant_vezes_que_pode_pedir_ajuda == 1:
            redefinir_lista_letra_das_alternativas()

        contabiliza_resultado()

    else:
        print()
        print('--'*20, 'Alternativa ERRADA', '--'*20)
        print('--' * tamanho_carac)
        if valor_do_premio == 1000000:
            print(f'Você ganhou R${valor_do_premio / 4:,.2f}')
            print()
            print('--' * tamanho_carac)
            tela_inicial()

        else:
            print(f'Você ganhou R${valor_do_premio / 2:,.2f}')
            print()
            print('--' * tamanho_carac)
            tela_inicial()


def validador_da_escolhar_opcao(escolha_opcao,pergunta_sorteada,embaralho):
    global quant_pulos,quant_vezes_que_pode_pedir_ajuda
    if escolha_opcao == '1':
        escolha_alternativa = input('Escolha uma alternativa: ').upper()
        escolha_alternativa = '('+ escolha_alternativa + ')'
        if escolha_alternativa in letras_das_alternativas:
            resposta_da_alternativa_escolhida = procurando_indice_da_alternativa_esolhida(escolha_alternativa,embaralho)
            resultado_da_resposta = validador_resposta_da_alternativa(resposta_da_alternativa_escolhida,pergunta_sorteada)
            reficador_da_resposta(resultado_da_resposta)
        else:
            print()
            print('--' * tamanho_carac)
            print('ERRO:')
            print('Escolha uma letra entre as acima: ')
            print('--' * tamanho_carac)
            imprime_pergunta(pergunta_sorteada)

    elif escolha_opcao == '2' and quant_pulos >= 3:
        quant_vezes_que_pode_pedir_ajuda += 1
        if quant_vezes_que_pode_pedir_ajuda <= 1:
            nova_lista_com_as_alternativas_removidas = remove_alternativa(pergunta_sorteada)
            imprime_pergunta(nova_lista_com_as_alternativas_removidas)


    elif escolha_opcao == '2':
        quant_pulos += 1
        if quant_vezes_que_pode_pedir_ajuda == 1:
            redefinir_lista_letra_das_alternativas()

        if quant_pulos >= 1 and quant_pulos <= 3:
            sorteado_de_novas_perguntas()


    elif escolha_opcao == '3':
        quant_vezes_que_pode_pedir_ajuda += 1
        if quant_vezes_que_pode_pedir_ajuda == 1:
            nova_lista_com_as_alternativas_removidas = remove_alternativa(pergunta_sorteada)
            imprime_pergunta(nova_lista_com_as_alternativas_removidas)


def imprime_erro_caso_a_opcao_Escolhida_esteja_erada(pergunta_sorteada):

    print()
    print('--'*tamanho_carac)
    print('ERRO:')
    print('Escolha um número entre os acima: ')
    print('--'*tamanho_carac)
    imprime_pergunta(pergunta_sorteada)


def verificador_opcoes_disponiveis_para_o_jogador(pergunta_sorteada, embaralho):
    if quant_pulos < 3 and quant_vezes_que_pode_pedir_ajuda < 1 and quant_acertos != 4:
        print()
        print('O que você deseja? ')
        print()
        print('[1] RESPONDER PERGUNTA  [2] PULAR PERGUNTA  [3] PEDIR AJUDA')
        print()
        escolha_opcao = input('Escolha uma opção: ')
        if escolha_opcao == '1' or escolha_opcao == '2' or escolha_opcao == '3':
            validador_da_escolhar_opcao(escolha_opcao, pergunta_sorteada, embaralho)

        else:
            imprime_erro_caso_a_opcao_Escolhida_esteja_erada(pergunta_sorteada)


    elif quant_pulos < 3 and quant_vezes_que_pode_pedir_ajuda == 1 and quant_acertos != 4:
        print()
        print('O que você deseja? ')
        print()
        print('[1] RESPONDER PERGUNTA  [2] PULAR PERGUNTA ')
        print()
        escolha_opcao = input('Escolha uma opção: ')
        if escolha_opcao == '1' or escolha_opcao == '2':
            validador_da_escolhar_opcao(escolha_opcao, pergunta_sorteada, embaralho)

        else:
            imprime_erro_caso_a_opcao_Escolhida_esteja_erada(pergunta_sorteada)

    elif quant_pulos == 3 and quant_vezes_que_pode_pedir_ajuda < 1 and quant_acertos != 4:
        print()
        print('O que você deseja? ')
        print()
        print('[1] RESPONDER PERGUNTA  [2] PEDIR AJUDA')
        print()
        escolha_opcao = input('Escolha uma opção: ')
        if escolha_opcao == '1' or escolha_opcao == '2':
            validador_da_escolhar_opcao(escolha_opcao, pergunta_sorteada, embaralho)

        else:
            imprime_erro_caso_a_opcao_Escolhida_esteja_erada(pergunta_sorteada)


    elif quant_pulos == 3 and quant_vezes_que_pode_pedir_ajuda == 1 and quant_acertos != 4:
        print()
        print('O que você deseja? ')
        print()
        print('[1] RESPONDER PERGUNTA ' )
        print()
        escolha_opcao = input('Escolha uma opção: ')
        if escolha_opcao == '1':
            validador_da_escolhar_opcao(escolha_opcao, pergunta_sorteada, embaralho)

        else:
            imprime_erro_caso_a_opcao_Escolhida_esteja_erada(pergunta_sorteada)

    elif quant_acertos == 4:
        print()
        print('O que você deseja? ')
        print()
        print('[1] RESPONDER PERGUNTA  [2] Desistir')
        print('Ao desistir você recebera R$ 500.000,00')
        print()
        escolha_opcao = input('Escolha uma opção: ')
        if escolha_opcao == '1':
            validador_da_escolhar_opcao(escolha_opcao,pergunta_sorteada,embaralho)

        elif escolha_opcao == '2':
            print('Você escolheu desistir.')
            print('Seu premio é de R$ 500.000,00')
            print('PARABÉNS')
            print()
            tela_inicial()

        else:
            imprime_erro_caso_a_opcao_Escolhida_esteja_erada(pergunta_sorteada)


def imprime_pergunta(pergunta_sorteada):
    embaralho = embaralhando_alternativas(pergunta_sorteada)
    print(f'Pergunta valendo: R${valor_do_premio:,.2f}')
    print()
    print(pergunta_sorteada[0])
    print()
    cont = 0
    for i in embaralho:
        print(f'{letras_das_alternativas[cont]} ', i )
        cont += 1
    verificador_opcoes_disponiveis_para_o_jogador(pergunta_sorteada, embaralho)


def sorteado_de_novas_perguntas():
    pergunta_sorteada = sorteia_pergunta(quant_acertos)
    imprime_pergunta(pergunta_sorteada)


def redefinindo_valores_iniciais():
    global valor_do_premio, quant_acertos, quant_pulos, quant_vezes_que_pode_pedir_ajuda
    valor_do_premio = 1000
    quant_acertos = 0
    quant_pulos = 0
    quant_vezes_que_pode_pedir_ajuda = 0


def validacao_escolha_inicial(escolha_inicial):

    if escolha_inicial == '1' or escolha_inicial == '2':
        if escolha_inicial == '1':
            preenche_niveis()
            if quant_vezes_que_pode_pedir_ajuda == 1:
                redefinir_lista_letra_das_alternativas()

            redefinindo_valores_iniciais()
            sorteado_de_novas_perguntas()

    else:
        print()
        print('ERRO:')
        print('Escolha um número entre 1 e 2: ')
        print('--' * tamanho_carac)
        menu_inicial()


def menu_inicial():
    print('-Iniciar Jogo    [1]')
    print('-Sair            [2]')
    print()
    escolha_inicial = input('O que você deseja? ')
    print('--'*tamanho_carac)
    validacao_escolha_inicial(escolha_inicial)


def tela_inicial():
    print()
    print('$-'*tamanho_carac)
    print('--'*21,'JOGO DO MILHÃO','--'*21)
    print('$-'*tamanho_carac)
    print()
    menu_inicial()


tela_inicial()
