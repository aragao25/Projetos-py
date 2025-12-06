# try:
#     x = 0
#     fim = int(input("digite ate que numero deseja contar: "))
#     while x <= fim:
#         print(x)
#         x += 1
# except:
#     print("digite somente um numero inteiro")
# animais = ('cachorro', 'gato', 'papagaio')
# print("\nPercorrendo a tupla com for:")
# for i, animal in enumerate(animais):
#     print(f"Animal {i}:", animal)

# def calcular_raiz_quadrada(numero):
#     if numero < 0:
#         # Dispara a exceção ValueError com uma mensagem
#         raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
#     return numero ** 0.5
#
# # Teste
# try:
#     resultado = calcular_raiz_quadrada(-4)
# except ValueError as e:
#     print(f"Erro capturado: {e}")
vingadores = ['homem de ferro', 'hulk', 'capitão américa', 'vúva negra', 'gavião arqueiro']
vingadores1 = vingadores.pop()
# vingadores.insert(1, vingadores1)
# print(vingadores)
# print(vingadores1)
di = {'julio': 'c', 'jaime': 'python', 'ana': 'ruby', 'claudia': 'java', 'mauro': 'php'}
x = di.items()
print(x)
for k, v in x:
    print(f" chave: {k}, valor: {v}")