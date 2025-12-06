def obter_contagem(item):
    """
    Função auxiliar usada pela função sorted() para extrair o valor de contagem.
    'item' é uma tupla (clube, contagem).
    Retorna o segundo elemento (o número de torcedores).
    """
    # Retorna o elemento no índice 1 da tupla (a contagem)
    return item[1]

def contar_torcedores_puro(nome_arquivo='pessoas.csv'):
    """
    Lê um arquivo CSV, conta torcedores e exibe em ordem decrescente,
    sem usar bibliotecas externas ou funções lambda.
    """

    # Dicionário para armazenar a contagem: {nome_do_clube: numero_de_torcedores}
    contagem_clubes = {}

    try:
        # Abre o arquivo para leitura (melhor prática com 'with')
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:

            # 1. Leitura e Contagem

            # Pula o cabeçalho (primeira linha)
            try:
                arquivo.readline()
            except:
                print(f"O arquivo '{nome_arquivo}' está vazio.")
                return

            # Itera sobre o restante das linhas
            for linha in arquivo:
                # Processamento da linha: remover espaços, quebrar pela vírgula
                dados = linha.strip().split(',')

                # Assumindo que o nome do clube está na 6ª coluna (índice 5)
                if len(dados) > 5:
                    # Normaliza o nome do clube (remove espaços e converte para MAIÚSCULAS)
                    nome_clube = dados[5].strip().upper()

                    # Atualiza a contagem no dicionário
                    if nome_clube in contagem_clubes:
                        contagem_clubes[nome_clube] += 1
                    else:
                        contagem_clubes[nome_clube] = 1

        # 2. Ordenação dos Resultados

        # Converte o dicionário em uma lista de tuplas (clube, contagem)
        lista_resultados = list(contagem_clubes.items())

        # Ordena a lista usando a função 'sorted'.
        # A chave de ordenação (key) agora aponta para a função 'obter_contagem',
        # que faz o mesmo trabalho que a função lambda fazia: retorna a contagem [1].
        resultados_ordenados = sorted(lista_resultados, key=obter_contagem, reverse=True)

        # 3. Exibição dos Resultados

        print(f"\n Resultados da Contagem de Torcedores no arquivo '{nome_arquivo}':")
        print("-" * 50)

        if not resultados_ordenados:
            print("Nenhum clube encontrado para contagem.")
            return

        for clube, torcedores in resultados_ordenados:
            # Formatação
            print(f"| {clube:<30} | {torcedores:>10} Torcedores |")

        print("-" * 50)

    except FileNotFoundError:
        print(f"🚨 Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")


# Executa a função principal
contar_torcedores_puro()