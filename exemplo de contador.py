# 1. Definição de uma Função
def verificar_par_impar(numero):
    """
    Verifica se um número é par ou ímpar.
    """
    # Estrutura de controle: IF/ELSE
    if numero % 2 == 0:
        return f"O número {numero} é PAR."
    else:
        return f"O número {numero} é ÍMPAR."


# ---

# 2. Dados de Entrada (Lista)
lista_de_numeros = [10, 7, 22, 15, 4, 99]

# 3. Processamento (Loop e Chamada da Função)
print("--- Verificação da Lista de Números ---")

# Estrutura de controle: FOR Loop
for num in lista_de_numeros:
    # Chama a função para cada item da lista
    resultado = verificar_par_impar(num)

    # Imprime o resultado
    print(resultado)