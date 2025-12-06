entrada_2 = []
entrada_0 = int(input("Digite a quantidade de números: "))

if 2 <= entrada_0 <= 1000:
    nomes = input("Digite os nomes separados por vírgula: ").split(", ")

    for i in nomes:
        nome = i
        valor = len(i)
        if 2 <= valor <= 19:
            entrada_2.append(nome)

# -------------------------------------------------------------------
# AGRUPANDO POR TAMANHO
# -------------------------------------------------------------------

grupos = {}
for nome in entrada_2:
    tamanho = len(nome)
    if tamanho not in grupos:
        grupos[tamanho] = []
    grupos[tamanho].append(nome)

# -------------------------------------------------------------------
# OBTENDO TAMANHOS ORDENADOS E MAX_LINHAS (Sem usar max/min)
# -------------------------------------------------------------------

tamanhos = sorted(grupos.keys())

max_linhas = 0  # Inicializa o contador de linhas
for t in grupos:
    tamanho_do_grupo = len(grupos[t])
    if tamanho_do_grupo > max_linhas:
        max_linhas = tamanho_do_grupo  # Encontra o máximo manualmente

# -------------------------------------------------------------------
# MONTAR SAÍDA USANDO "insert"
# -------------------------------------------------------------------

linhas = []

for i in range(max_linhas):
    linha = []
    for t in tamanhos:
        if i < len(grupos[t]):
            # USANDO INSERT: Adiciona o nome ao final da lista `linha`.
            linha.insert(len(linha), grupos[t][i])

    # Se a linha não for vazia (ou seja, se houver nomes para esta linha), adicione
    # (Embora não seja estritamente necessário neste caso, garante que linhas totalmente vazias não sejam adicionadas se houver um erro de lógica)
    if linha:
        linhas.append(linha)

    # -------------------------------------------------------------------
# IMPRIMIR SAÍDA (Sem usar sep)
# -------------------------------------------------------------------

for linha in linhas:
    # Cria uma string com vírgula e espaço (", ") manualmente.
    # O método join faz a mesma função que o sep faria no print.
    print(", ".join(linha))
