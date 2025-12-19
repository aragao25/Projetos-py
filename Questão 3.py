# Questão 3. Desenvolva um programa que leia um arquivo pessoas.csv contendo nomes e os
# clubes para os quais cada pessoa torce. O programa deverá contar quantas pessoas torcem para
# cada clube e exibir os resultados em ordem decrescente, do clube com mais torcedores para o que
# tem menos.

#Este código é um exemplo clássico de como processar dados de um arquivo e calcular frequências em Python.

contagem_times = {} #Inicializa um dicionário vazio. Este dicionário será usado para armazenar
# a contagem de torcedores por time. A chave será o nome do time, e o valor será o número de pessoas que torcem para ele.

lista_dicionarios = [] #Inicializa uma lista vazia. Embora seja inicializada aqui, ela é re-inicializada dentro da função ler_csv_para_dicionario,
# então esta inicialização externa não é estritamente necessária para a lógica de contagem final.

def ler_csv_para_dicionario(pessoas): #Esta função é responsável por ler o conteúdo de um arquivo CSV e converter cada linha de dados (exceto o cabeçalho)
    # em um dicionário, onde as chaves são os nomes das colunas (cabeçalho) e os valores são os dados da linha.
    lista_dicionarios = []
    with open('pessoas.csv', 'r') as arquivo: #Abre o arquivo pessoas.csv no modo de leitura ('r'). O bloco with open(...) garante que o arquivo
    # seja automaticamente fechado após a execução.

        linhas = arquivo.readlines() #Lê todas as linhas do arquivo e as armazena na lista linhas.
    if not linhas: #Verifica se o arquivo está vazio. Se sim, retorna a lista vazia imediatamente.
        return lista_dicionarios

    chaves = linhas[0].strip().split(",") #Pega a primeira linha (o cabeçalho), remove espaços em branco/quebras de linha (strip())
    # e divide a string em uma lista de strings usando a vírgula (,) como separador (split(",")).
    # Esta lista de strings se tornará as chaves dos dicionários.

    for linha in linhas[1:]: #Itera sobre as linhas restantes, começando da segunda linha (linhas[1:]), que são os dados.
        valores = linha.strip().split(",") #Processa cada linha de dados da mesma forma que o cabeçalho, obtendo a lista de valores para aquela pessoa.

        if len(chaves) == len(valores): #Uma verificação de segurança para garantir que o número de colunas do cabeçalho corresponde ao número de valores
        # na linha de dados (evitando erros em linhas mal-formadas).

            dicionario_linhas = dict(zip(chaves, valores)) #Usa a função zip() para combinar a lista de chaves (cabeçalho) com a lista de valores da linha atual e,
        # em seguida, cria um dicionário a partir dessa combinação.

            lista_dicionarios.append(dicionario_linhas) #Adiciona o dicionário recém-criado à lista.

    return lista_dicionarios #Retorna a lista completa de dicionários de dados.

dados = ler_csv_para_dicionario('pessoas.csv') #Executa a função para ler o CSV e armazena o resultado (a lista de dicionários) na variável dados.
# print(dados)

# Itera sobre cada pessoa na lista
for pessoa in dados: #Inicia um loop que passa por cada dicionário (pessoa) dentro da lista dados.
    time = pessoa['Time que torce'] #Para cada dicionário (pessoa), extrai o valor associado à chave 'Time que torce'. Assumimos que esta coluna existe no CSV.

    # Usa o .get() para obter a contagem atual (ou 0 se for o primeiro) e adiciona 1.
    contagem_times[time] = (contagem_times.get(time, 0) + 1)
#contagem_times[time] = (contagem_times.get(time, 0) + 1): Esta é a parte principal da contagem:
#contagem_times.get(time, 0): Tenta obter a contagem atual para o time em contagem_times.
# Se o time ainda não estiver no dicionário (ou seja, é o primeiro torcedor desse time), ele retorna o valor padrão de 0.
#+ 1: Adiciona 1 à contagem (atual ou 0).
#contagem_times[time] = ...: Atualiza/Insere o novo valor de contagem no dicionário contagem_times, usando o nome do time como chave.
#print(contagem_times): Imprime o dicionário final com a contagem de torcedores para cada time.

# print(contagem_times)

def pegar_contagem(item):#Define uma função simples que recebe um item (que será uma tupla (chave, valor)) e retorna o segundo elemento (item[1]),
    # que é o valor da contagem. Esta função será usada como a chave de classificação.

    return item[1]
times_ordenados = sorted(contagem_times.items(), key=pegar_contagem, reverse=True)
# contagem_times.items():Converte o dicionário contagem_times em uma lista de tuplas
# (time, contagem). Exemplo: [('Flamengo', 5), ('Corinthians', 3)].
#  sorted(...): Classifica a lista de tuplas.
# key=pegar_contagem: Diz à função sorted() para usar o segundo elemento da tupla (a contagem, que é o resultado de pegar_contagem(item)) como base para a classificação.
# reverse=True: Indica que a classificação deve ser em ordem decrescente (do time com mais torcedores para o time com menos).
# O resultado é armazenado em times_ordenados.

for time, contagem in times_ordenados: # Itera sobre a lista de tuplas ordenada.
    print(f"- {time}: {contagem}")

# print(f"- {time}: {contagem}"): Imprime o resultado final em um formato legível: o nome do time e sua contagem de torcedores.
