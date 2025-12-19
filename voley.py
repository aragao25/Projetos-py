# VARIÁVEIS PARA ACUMULAR OS TOTAIS (Inicialização):
s_total = 0  # soma os totais de tentativas de saque
b_total = 0  # soma os totais de tentativas de bloqueio
a_total = 0  # soma os totais de tentativas de ataque
s1_total = 0  # soma os totais de saque bem sucedidos
b1_total = 0  # soma os totais de bloqueio bem sucedidos
a1_total = 0  # soma os totais de ataque bem sucedidos

# --- INICIA O CÓDIGO ---
try:
    n = int(input("Digite o números de jogadores: "))
except ValueError:
    print("Entrada inválida. O número de jogadores deve ser um inteiro.")
    exit()

# ESTRUTURA DE REPETIÇÃO PARA LER A QUANTIDADE DE JOGADORES
for i in range(n):
    print(f"\n--- Jogador {i + 1} de {n} ---")
    nome_jogador = input("Digite o nome do jogador: ")

    # 1. ENTRADA DE N.º DE TENTATIVAS (S, B, A)

    print(f"Digite as tentativas (S, B, A) do {nome_jogador} separadas por espaço: ")
    s, b, a = map(int, input().split()) # recebe e separa e transforma para inteiros os valores e atribui as variáveis s,b,a

    # 2. ENTRADA DE N.º DE JOGADAS SUCEDIDAS (S1, B1, A1)

    print(f"Digite as jogadas bem sucedidas (S1, B1, A1) do {nome_jogador} separadas por espaço: ")
    s1, b1, a1 = map(int,
                     input().split())  # input lê a string, .split divide em substrings e map(int,) cria uma lista de númeroa inteiros

    # 3. ACUMULAÇÃO DOS TOTAIS DA EQUIPE
    s_total += s
    b_total += b
    a_total += a

    s1_total += s1
    b1_total += b1
    a1_total += a1


# --- FIM DO LOOP 'for' ---

# FUNÇÃO: DEFINIDA UMA ÚNICA VEZ APÓS O LOOP
def calcula_percentual(jogadas_sucedidas: int | float, jogadas_tentativas: int | float) -> float:
    if jogadas_tentativas == 0:
        return 0.0
    return (jogadas_sucedidas / jogadas_tentativas) * 100


# CÁLCULO FINAL E SAÍDA: EXECUTADO UMA ÚNICA VEZ
print("\n--- Resultados Finais da Equipe ---")

# 1. Cálculo saque
perc_saque = calcula_percentual(s1_total, s_total)
print(f"Pontos de Saque: {perc_saque:.2f} %.")

# 2. Cálculo bloqueio
perc_bloqueio = calcula_percentual(b1_total, b_total)
print(f"Pontos de Bloqueio: {perc_bloqueio:.2f} %.")

# 3. Cálculo ataque
perc_ataque = calcula_percentual(a1_total, a_total)
print(f"Pontos de Ataque: {perc_ataque:.2f} %.")