# Questão 94. Escreva um algoritmo para repetir a leitura de uma senha até que ela seja válida.
# # Para cada leitura da senha incorreta informada escrever a mensagem "SENHA INVÁLIDA". Quanto
# # a senha for informada corretamente deve ser impressa a mensagem "ACESSO PERMITIDO"e o
# # algoritmo é encerrado mostrando quantas vezes a senha foi digitada. Considere que a senha
# # correta o valor 2014.

tentativa: int = 0
senha = int(input("Digite a senha: "))
if senha == 2014:
    print("Acesso permitido!")
    tentativa
else:
    print("Acesso negado!")

    while tentativa > 0:
        print("Acesso negado!")
    tentativa += 1
print("Quantidades de tantativas de acesso: ", tentativa))







