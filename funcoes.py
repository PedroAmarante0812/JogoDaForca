import os
import time

def limparTela():
    os.system("cls")

def aguarde(segundos=1):
    time.sleep(segundos)

def lerInteiro(mensagem):
    while True:
        try:
            variavel = int(input(mensagem))
            return variavel
        except:
            print("Valor informado incorretamente!")

def lerString(mensagem):
    while True:
        variavel = input(mensagem)
        if len(variavel)>1:
            return variavel
        else:
            print("Valor informado incorretamente!")
        
def quebralinha():
    print("\n")

def historico():
    try:
        arquivo = open("his.jogos","r")
        dados = arquivo.read()
        print(dados)
        arquivo.close()
        aguarde(5)
    except:
        print("Nenhuma partida encontrado")
        arquivo = open("his.jogos","w")
        arquivo.close()
        aguarde(2)

def removerAcentos(texto):
    acentos = {
        'á': 'a',
        'à': 'a',
        'â': 'a',
        'ã': 'a',
        'é': 'e',
        'ê': 'e',
        'í': 'i',
        'ó': 'o',
        'ô': 'o',
        'õ': 'o',
        'ú': 'u',
        'ü': 'u',
        'ç': 'c'
    }
    for acento, sem_acento in acentos.items():
        texto = texto.replace(acento, sem_acento)
    return texto