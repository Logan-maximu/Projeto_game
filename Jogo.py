from time import sleep

def Perguntas():
    perguntando = True
    Valor_ganho = 0

    while perguntando:
        print("PERGUNTA NUMERO 1")
        print("Para quantos tipos sanguíneos o tipo O+ pode doar?")
        sleep(1)
        print('[Alternativa 1] - 1 Tipo ')
        sleep(1)
        print('[Alternativa 2] - 2 tipos ')
        sleep(1)
        print('[Alternativa 3] - 4 tipos ')
        sleep(1)
        print('[Alternativa 4] - Nenhum tipo ')
        sleep(1)

        questao_1 = int(input("Digite sua resposta: "))
        if questao_1 == 3:
            print("Certa Resposta")
            print("O tipo sanguíneo O+ é compatível com todos os positivos, totalizando 4 tipos")
            print()
            sleep(1)
            Valor_ganho += 1000000
            print('Voce possui R$', Valor_ganho)
            while True:
                continuar = str(input('Deseja parar e ficar com seu o valor ou continuar e arricar perder tudo? [S/N]  ')).upper()[0]  # Pergunta se deseja continuar
                if continuar in 'SN':  # Garante que os valores sejam S ou N
                    break  # Para o loop
                print('ERRO! Responda apenas S ou N.')  # Imprime mensagem de erro
            if continuar  == 'S':
                print("\nPARABÉNS! Você ganhou R$", Valor_ganho )
                break

            print()

        else:
            print("Resposta errada!")
            print("O tipo sanguíneo O+ é compatível com todos os positivos, totalizando 4 tipos, a resposta correta era [Alternativa 2] - 4 tipos")
            break

        print("PERGUNTA NUMERO 2")
        sleep(1)
        print("Qual a proteína responsavel pela coloração do corpo?")
        sleep(1)
        print(' [Alternativa 1] - Melanina ')
        sleep(1)
        print('[Alternetiva 2] - Caseína')
        sleep(1)
        print('[Alternativa 3] - Actina')
        sleep(1)
        print('[Alternativa 4] - Miosina')
        sleep(1)

        questao2 = int(input("Digite sua resposta: "))
        if questao2 == 1:
            print("Certa resposta")
            print("A proteína responsável pela coloração do corpo é nomeada de Melanina produzida pela Tirosina")
            print()
            Valor_ganho += 1000000
            print('Voce possui R$', Valor_ganho)
            while True:
                continuar = \
                str(input('Deseja parar e ficar com seu o valor ou continuar e arricar perder tudo? [S/N]  ')).upper()[
                    0]  # Pergunta se deseja continuar
                if continuar in 'SN':  # Garante que os valores sejam S ou N
                    break  # Para o loop
                print('ERRO! Responda apenas S ou N.')  # Imprime mensagem de erro
            if continuar == 'S':
                print("\nPARABÉNS! Você ganhou", Valor_ganho)
                break
        else:

            print("Resposta errada!")
            print("A proteína responsável pela coloração do corpo é nomeada de Melanina, que é produzida pela Tirosina.")
            break

        print("\nPERGUNTA NUMERO 3")
        sleep(1)
        print("Qual o fator que o corpo de um diabético não reproduz?")
        sleep(1)
        print('[Alternativa 1] - Sacarose')
        sleep(1)
        print('[Alternativa 2] - Maltose')
        sleep(1)
        print('[Alternativa 3] - Celulose')
        sleep(1)
        print("[Alternativa 4] - Insulina")
        sleep(1)

        questao3 = int(input("Digite sua resposta: "))

        if questao3 == 4:
            print("Certa resposta")
            print( "A insulina é um hormônio que o corpo de um diabético não produz o suficiente e por isso a glicose não é metabolizada")
            print()
            sleep(1)
            Valor_ganho += 1000000
            print('Voce possui R$', Valor_ganho)
            while True:
                continuar = \
                str(input('Deseja parar e ficar com seu o valor ou continuar e arricar perder tudo? [S/N]  ')).upper()[
                    0]  # Pergunta se deseja continuar
                if continuar in 'SN':  # Garante que os valores sejam S ou N
                    break  # Para o loop
                print('ERRO! Responda apenas S ou N.')  # Imprime mensagem de erro
            if continuar == 'S':
                print("\nPARABÉNS! Você ganhou", Valor_ganho)
                break
        else:
            print("Resposta errada!")
            print("A proteína responsável pela coloração do corpo é nomeada de Melanina, que é produzida pela Tirosina.")
            break

        print("PERGUNTA NUMERO 4")
        sleep(1)
        print('"O sexo pode trazer muitos benefícios para a vida do homem e da mulher, quais desses a seguir não é um desses benefícios?')
        sleep(1)
        print('[Alternativa 1] - Sistema Imunológico')
        sleep(1)
        print('[Alternativa 2] - Sono ')
        sleep(1)
        print('[Alternativa 3] - Produção de Glicose')
        sleep(1)
        print('[Alternativa 4] - Produção de Ocitocina')
        sleep(1)


        questao4 = int(input("Digite sua resposta: "))
        if questao4 == 3:
            print("Certa reposta")
            print("O sexo ajuda muito na vida dos adultos, porém a produção de glicose não é um benefício e por isso, é a única das alternativas que não é um benefício do mesmo")
            print()
            sleep(1)
            Valor_ganho += 1000000
            print('Voce possui R$', Valor_ganho)
            while True:
                continuar = \
                str(input('Deseja parar e ficar comseu o valor ou continuar e arricar perder tudo? [S/N]  ')).upper()[
                    0]  # Pergunta se deseja continuar
                if continuar in 'SN':  # Garante que os valores sejam S ou N
                    break  # Para o loop
                print('ERRO! Responda apenas S ou N.')  # Imprime mensagem de erro
            if continuar == 'S':
                print("\nPARABÉNS! Você ganhou", Valor_ganho)
                break
        else:
            print("Resposta errada!")
            print("Dentre todos os benefícios, a produção de glicose não se aplica como um, então a resposta certa sera a [Alternativa 3] - Produção de Clicose")
            break

        print("PERGUNTA NUMERO 5")
        print("É recomendado que prática ao levantar da cama?")
        print('[Alternativa 1] - Flexão')
        print('[Alternativa 2] - Abdominal')
        print('[Alternativa 3] - Banho')
        print('[Alternativa 4] - Alongamento')

        questao5 = int(input("Digite sua resposta: "))
        if questao5 == 4:
            print("Certa resposta")
            print("Ao acordar, é recomendado que façamos um alongamento, para que assim, nossos músculos possam ser preparados para a rotina do dia, por isso, é muito importante esta atividade ao acordar")
            print("\nPARABÉNS! Você ganhou", Valor_ganho)
            print("\nObrigado por jogar o nosso jogo! Aperte qualquer tecla para encerrar a janela! <3")
            while True:
                jogardenovo = str(input('Deseja jogar novamente? [S/N]  ')).upper()[0]  # Pergunta se deseja continuar
                if jogardenovo in 'SN':  # Garante que os valores sejam S ou N
                    break  # Para o loop
                print('ERRO! Responda apenas S ou N.')  # Imprime mensagem de erro
                if jogardenovo == 'S':
                    perguntando = True
                else:
                    print("\nObrigado por jogar o nosso jogo! Aperte qualquer tecla para encerrar a janela! <3")
                    break





        else:
            print("Resposta errada!")
            print("Ao acordar, é muito importante alongar seu corpo para preparar os músculos para o estímulo do dia, por isso, a resposta certa seria [Alternativa 4] - Alongamento")
            while True:
                jogardenovo = str(input('Deseja jogar novamente? [S/N]  ')).upper()[0]  # Pergunta se deseja continuar
                if jogardenovo in 'SN':  # Garante que os valores sejam S ou N
                    break  # Para o loop
                print('ERRO! Responda apenas S ou N.')  # Imprime mensagem de erro
                if jogardenovo == 'S':
                    perguntando = True
                else:
                    print("\nObrigado por jogar o nosso jogo! Aperte qualquer tecla para encerrar a janela! <3")
                    break



jogo = Perguntas()
print(jogo)
