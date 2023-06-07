
from funcoes import *

while True:
    limparTela()
    print("Bem-vindo ao jogo da forca")
    print("pressione algum dos números para continuar")
    print("(1) Jogar")
    print("(2) Histórico de jogos")
    print("(3) Sair")
    escolha = input(" ")
    if escolha == "1":
        limparTela()
        print("Vamos começar! Qual é o nome do desafiante e do competidor?")
        desafiante = input("Desafiante: ")
        competidor = input("Competidor: ")
        limparTela()
        quebralinha()
        print("----------Ok, Desafiante",desafiante+", vamos dar ínicio----------")
        palavraChaveComAcento = input("Qual é a Palavra-Chave dessa partida? ")
        palavraChaveComAcento = palavraChaveComAcento.lower()   #Lembrete: .lower deixa as letras em minusculo
        palavraChave = removerAcentos(palavraChaveComAcento)

        print("Precisamos de 3 dicas para ajudar o Competidor, quais seriam?")
        dicas = []
        dica1 = input("Dica 1: ")
        dicas.append(dica1)
        dica2 = input("Dica 2: ")
        dicas.append(dica2)
        dica3 = input("Dica 3: ")
        dicas.append(dica3)
        limparTela()
        vidas = 6
        certas = []
        erradas = []
        quebralinha()
        print("----------Tudo pronto, Competidor",competidor+", agora é com você----------")
        while True:
            for letra in palavraChave:
                if letra in certas:
                    print(letra, end=" ")
                else:
                    print("_", end=" ")
            quebralinha()
            if vidas == 6:
                print("    _____\n   |     |\n         |\n         |\n         |\n         |\n         |\n  _______|\n")
            elif vidas == 5:
                print("    _____\n   |     |\n   O     |\n         |\n         |\n         |\n         |\n  _______|\n")
            elif vidas == 4:
                print("    _____\n   |     |\n   O     |\n   |     |\n         |\n         |\n         |\n  _______|\n")
            elif vidas == 3:
                print("    _____\n   |     |\n   O     |\n  /|     |\n         |\n         |\n         |\n  _______|\n")
            elif vidas == 2:
                print("    _____\n   |     |\n   O     |\n  /|\\    |\n         |\n         |\n         |\n  _______|\n")
            elif vidas == 1:
                print("    _____\n   |     |\n   O     |\n  /|\\    |\n  /      |\n         |\n         |\n  _______|\n")
            else:
                print("    _____\n   |     |\n   O     |\n  /|\\    |\n  / \\    |\n         |\n         |\n  _______|\n")
                print(competidor,"Você perdeu! A palavra era:",palavraChave)
                print("O desafiante",desafiante,"ganhou esse jogo!")
                arquivo = open("his.jogos","a")
                arquivo.write(f"\nVitoria do Desafiante {desafiante} sobre o Competidor {competidor}, pela palavra {palavraChave}")
                print("Histórico de jogo salvo!")
                arquivo.close()
                arquivo = open("his.jogos","r")
                dados = arquivo.read()
                arquivo.close()
                print("Histórico das últimas partidas:")
                print(dados)
                deNovo = input("Voltar a tela inicial? (S)sim ou (N)não: ")
                if deNovo == "s":
                    aguarde(1)
                    break
                else:
                    print("Encerrando os jogos! Obrigado por jogar...")
                    aguarde(3)
                    exit()
            print("Letras erradas: ", erradas)
            print("Vidas restantes:", vidas)
            if len(dicas) == 3:
                print("Você possui",str(len(dicas)),"dicas! O que prefere?")
            elif len(dicas) >= 1:
                print("Escolha uma das opções abaixo!")
            else:
                print("Suas dicas acabaram!")
            if len(dicas) == 3:
                print("(1) Jogar")
                print("(2) Solicitar Dica")
                decisaoJogador = input(" ")
                if decisaoJogador == "1":
                    pass
                elif decisaoJogador == "2":
                    print("Sua primeira dica é:",dicas[0])
                    dicas.pop(0)
                else:
                    pass
            elif len(dicas) == 2:
                print("(1) Jogar")
                print("(2) Você tem 2 dicas, deseja usá-la?")
                decisaoJogador = input(" ")
                if decisaoJogador == "1":
                    pass
                elif decisaoJogador == "2":
                    print("Sua segunda dica é:",dicas[0])
                    dicas.pop(0)      
            elif len(dicas) == 1:
                print("(1) Jogar")
                print("(2) Essa é sua última dica, quer usá-la agora?")
                decisaoJogador = input(" ")
                if decisaoJogador == "1":
                    pass
                elif decisaoJogador == "2":
                    print("Sua última dica é:",dicas[0])
                    dicas.pop(0)  
            elif len(dicas) == 0:
                pass
            else:
                pass
            chuteLetra = input("Qual é sua tentativa? ").lower()

            if chuteLetra in certas or chuteLetra in erradas:
                limparTela()
                print("Você já tentou essa letra. Tente outra.")
            elif chuteLetra in palavraChave:
                certas.append(chuteLetra)
                limparTela()
                print("Acertou!")
            else:
                erradas.append(chuteLetra)
                vidas -= 1
                limparTela()
                print("Errou!")
            if set(certas) == set(palavraChave):
                print("Parabéns",competidor+". Você venceu! A palavra era:",palavraChave)
                print("Infelizmente o desafiante",desafiante,"perdeu esse jogo.")
                arquivo = open("his.jogos","a")
                arquivo.write(f"\nVitoria do Competidor {competidor} sobre o Desafiante {desafiante}, sobrando {int(vidas)} vidas da palavra: {palavraChave}")
                print("Histórico de jogo salvo!")
                arquivo.close()
                arquivo = open("his.jogos","r")
                dados = arquivo.read()
                arquivo.close()
                print("Histórico das últimas partidas:")
                print(dados)
                irDeNovo = input("Voltar a tela inicial? (S)sim ou (N)não: ")
                if irDeNovo == "s":
                    aguarde(1)
                    break
                else:
                    print("Encerrando os jogos! Obrigado por jogar...")
                    aguarde(3)
                    exit()
    elif escolha == "2":
        limparTela()
        try:
            arquivo = open("his.jogos","r")
            dados = arquivo.read()
            print(dados)
            arquivo.close()
            input("Pressione ENTER para continuar...")
            aguarde(1)
        except:
            print("Nenhum jogo encontrado")
            arquivo = open("his.jogos","w")
            arquivo.close()
            print("Histórico criado!")
            aguarde(2)
    elif escolha == "3":
        limparTela()
        exit()
    else:
        print("Opção Inexistente!")
        aguarde(2)