#Receba o nome, sobrenome, sexo, RG e idade e posteriormente exiba as informações na tela.
#Nome e sobrenome devem ser informados na mesma linha
nome = input("Digite o primeiro nome: ").strip().upper()
sobre_nome = input("Digite o sobre nome: ").strip().upper()
nome_completo = nome + " " + sobre_nome
sexo = input("Digite o sexo: ").strip().upper()
rg = int(input("Digite o nome do RG: ").strip().upper())
idade = int(input("Digite sua idade: ").strip().upper())
print(nome_completo)
print(sexo)
print(rg)
print(idade)
