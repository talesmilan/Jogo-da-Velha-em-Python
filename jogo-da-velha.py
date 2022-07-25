
#Função que faz a jogada do Jogador 1
def jogador1():
    encontrou = False
    print("Vez do jogador 1!")
    print("-----------------")
    jogada = int(input("Escolha um número de 1 a 9 e faça sua jogada: "))
    while jogada > 9 or jogada < 1:
        jogada = int(input("Jogada invalida escolha outro número: "))
    while not encontrou:
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if tabuleiro[i][j] == jogada:
                    tabuleiro[i][j] = "X"
                    encontrou = True
        if not encontrou:
            jogada = int(input("Esse número já foi escolhido, escolha outro: "))
    global jogadas
    jogadas = jogadas + 1

#Função que faz a jogada do Jogador 2
def jogador2():
    encontrou = False
    print("Vez do jogador 2!")
    print("-----------------")
    jogada = int(input("Escolha um número de 1 a 9 e faça sua jogada: "))
    while jogada > 9 or jogada < 1:
        jogada = int(input("Jogada invalida escolha outro número: "))
    while not encontrou:
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if tabuleiro[i][j] == jogada:
                    tabuleiro[i][j] = "O"
                    encontrou = True
        if not encontrou:
            jogada = int(input("Esse número já foi escolhido, escolha outro: "))
    global jogadas
    jogadas = jogadas + 1
    
#Função que mostra o tabuleiro
def mostrarTabuleiro():
    print("-----------------")
    for i in range(0, 3, 1):
        for j in range(0, 3 ,1):
            print("| " + str(tabuleiro[i][j]) + " | ", end = "")
        print()
    print("-----------------")

#Função que checa se o jogo acabou
def acabou():
    for i in range(3):
        if tabuleiro[i][0] == "X" and tabuleiro[i][1] == "X" and tabuleiro[i][2] == "X":
            return 1
        if tabuleiro[0][i] == "X" and tabuleiro[1][i] == "X" and tabuleiro[2][i] == "X":
            return 1
        if tabuleiro[i][0] == "O" and tabuleiro[i][1] == "O" and tabuleiro[i][2] == "O":
            return 2
        if tabuleiro[0][i] == "O" and tabuleiro[1][i] == "O" and tabuleiro[2][i] == "O":
            return 2
    if tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X":
        return 1
    if tabuleiro[0][2] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][0] == "X":
        return 1
    if tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O":
        return 2
    if tabuleiro[0][2] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][0] == "O":
        return 2
    if jogadas > 8:
        return 3
    return 0

#Código principal
tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]
vezDoJogador1 = True
jogadas = 0
print("-----------------")
print("  JOGO DA VELHA  ")
print("-----------------")
mostrarTabuleiro()
while acabou() == 0:
    if vezDoJogador1:
        jogador1()
        mostrarTabuleiro()
        vezDoJogador1 = False
    else:
        jogador2()
        mostrarTabuleiro()
        vezDoJogador1 = True
        
if acabou() == 1:
    print("O jogador 1 venceu!")
    print("-----------------")
elif acabou() == 2:
    print("O jogador 2 venceu!")
    print("-----------------")
else:
    print("Deu velha!")
    print("-----------------")
    