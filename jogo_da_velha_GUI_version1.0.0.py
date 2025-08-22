# Importa a biblioteca 'os' para limpar o terminal.
import os

# --- Funções do Jogo ---

# Função para exibir o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    """
    Exibe o tabuleiro do jogo no terminal.
    
    Args:
        tabuleiro (list): Uma lista de listas que representa o tabuleiro.
    """
    # Limpa o terminal para uma visualização mais limpa do tabuleiro a cada jogada.
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Jogo da Velha ---")
    print() # Linha em branco
    for linha in tabuleiro:
        print(" | ".join(linha))
        # Imprime uma linha divisória entre as linhas do tabuleiro.
        print("---------")
    print() # Linha em branco

# Função para verificar se há um vencedor
def verificar_vitoria(tab, jogador):
    """
    Verifica se o jogador atual venceu o jogo.
    
    Args:
        tab (list): O tabuleiro atual.
        jogador (str): O símbolo do jogador ('X' ou 'O').
    
    Returns:
        bool: True se o jogador venceu, False caso contrário.
    """
    # Verifica todas as linhas
    for i in range(3):
        # A função all() verifica se todos os elementos na lista são True.
        if all([celula == jogador for celula in tab[i]]):
            return True
            
    # Verifica todas as colunas
    for i in range(3):
        if all([tab[j][i] == jogador for j in range(3)]):
            return True
            
    # Verifica a diagonal principal (de cima para a esquerda para baixo para a direita)
    if all([tab[i][i] == jogador for i in range(3)]):
        return True
        
    # Verifica a diagonal secundária (de cima para a direita para baixo para a esquerda)
    if all([tab[i][2 - i] == jogador for i in range(3)]):
        return True
        
    return False

# Função principal que executa o jogo
def jogar_jogo_da_velha():
    """
    Função principal que coordena o fluxo do jogo.
    """
    # Inicializa o tabuleiro com as posições de 1 a 9.
    tabuleiro = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    
    jogador_atual = "X"  # O jogador X sempre começa.
    rodada = 0           # Contador de rodadas para verificar empate.

    # Loop principal do jogo. O jogo tem no máximo 9 jogadas.
    while rodada < 9:
        mostrar_tabuleiro(tabuleiro)
        
        # Loop para garantir que a entrada do jogador é válida.
        while True:
            escolha = input(f"Vez do jogador {jogador_atual}. Escolha uma posição (1-9): ")
            
            # Tenta converter a entrada para um número.
            if escolha.isdigit():
                pos = int(escolha) - 1
                
                # Verifica se o número está dentro do intervalo de 0 a 8.
                if 0 <= pos <= 8:
                    linha, coluna = pos // 3, pos % 3
                    
                    # Verifica se a posição escolhida já está ocupada.
                    if tabuleiro[linha][coluna] not in ["X", "O"]:
                        # Se a posição estiver livre, a jogada é válida.
                        tabuleiro[linha][coluna] = jogador_atual
                        break  # Sai do loop de entrada
                    else:
                        print("Posição já ocupada. Escolha outra.")
                else:
                    print("Entrada inválida. Digite um número de 1 a 9.")
            else:
                print("Entrada inválida. Digite um número.")
        
        # Após a jogada, verifica se o jogador atual venceu.
        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {jogador_atual} venceu!")
            return # Termina o jogo.
        
        rodada += 1
        
        # Alterna o jogador para a próxima rodada.
        jogador_atual = "O" if jogador_atual == "X" else "X"
        
    # Se o loop terminar sem um vencedor, o jogo é um empate.
    mostrar_tabuleiro(tabuleiro)
    print("Fim do jogo! Empate!")

# Inicia o jogo quando o script é executado.
if __name__ == "__main__":
    jogar_jogo_da_velha()