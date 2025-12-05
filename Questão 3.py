# Questão 3. Desenvolva um programa que leia um arquivo pessoas.csv contendo nomes e os
# clubes para os quais cada pessoa torce. O programa deverá contar quantas pessoas torcem para
# cada clube e exibir os resultados em ordem decrescente, do clube com mais torcedores para o que
# tem menos.
contador = 0
i=0
arquivo_nomes = []
tamanho = len(arquivo_nomes)
soma_nomes = 0
clube = input("Digite o nome de uma clube: ").upper()
with open('pessoas.csv', 'r') as arquivo:
    arquivo.readline()
    for linha in arquivo:
        dados = linha.split(',')
        if clube == dados[5].upper():
            arquivo_nomes.append(dados[0])
    for i in range(tamanho):
        soma_nomes = i + 1

        print(soma_nomes)



