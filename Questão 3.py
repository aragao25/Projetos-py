# Questão 3. Desenvolva um programa que leia um arquivo pessoas.csv contendo nomes e os
# clubes para os quais cada pessoa torce. O programa deverá contar quantas pessoas torcem para
# cada clube e exibir os resultados em ordem decrescente, do clube com mais torcedores para o que
# tem menos.
contador = 0
arquivo_nomes = []
with open('pessoas.csv', 'r') as arquivo:
