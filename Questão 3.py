# Questão 3. Desenvolva um programa que leia um arquivo pessoas.csv contendo nomes e os
# clubes para os quais cada pessoa torce. O programa deverá contar quantas pessoas torcem para
# cada clube e exibir os resultados em ordem decrescente, do clube com mais torcedores para o que
# tem menos.

def ler_csv_para_dicionario(pessoas.csv):
    lista_dicionarios = []
    with open(pessoas.csv, "r") as arquivo:
        linhas = aquivo.readlines()
    if not linhas:
        return lista_dicionarios
    chaves = linhas[0].strip().split(",")
    for linha in linhas[1:]:
        valores = linha.strip().split(",")
        if len(chaves) == len(valores):
        dicionario_linhas = dict(zip(chaves, valores))
        lista_dicionarios.append(dicionario_linhas)
    return lista_dicionarios
dados = ler_csv_para_dicionario('pessoas.csv')