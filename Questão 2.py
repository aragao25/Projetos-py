# Questão 2. Elabore um programa que leia o arquivo chamado pessoas.csv, contendo dados de

# várias pessoas, incluindo a cidade onde moram. O programa deve solicitar ao usuário que digite o

# nome de uma cidade e, em seguida, listar na tela todas as pessoas que residem nesta cidade.


contador = 0
arquivo_nomes = []
with open('pessoas.csv', 'r') as arquivo:

# solicita nome da cidade

    cidade = input("Digite o nome de uma cidade: ").upper()

# condições

    for linha in arquivo:
        dados = linha.split(',')
# nome = dados[0]
        if cidade == dados[3].upper():
            arquivo_nomes.append(dados[0])
            print(dados[0])
            contador = contador + 1

arquivo.close()

# lista na tela todas as pessoas que residem na cidade

print(f"Quantidade de pessoas em {cidade} é: {contador}")
# print(arquivo_nomes)
with open('nova_lista.csv', 'w') as arquivo1:
    for i in arquivo_nomes:

        arquivo1.write(f"{i} \\n")


arquivo1.close()
