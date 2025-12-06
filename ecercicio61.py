# Questão 61. Para doar sangue é necessário ter entre 18 e 67 anos, pesar mais de 50kg e estar
# em jejum. Faça um programa que pergunta para 10 usuários a idade, peso do usuário e se ele está
# em jejum, diga se o usuário pode doar sangue ou não. No final, indica quantos usuários são
# doadores e quantos não são.

idades = [18, 20, 10, 17, 70, 45, 32, 21, 50, 25]
pesos = [50, 30, 49, 78, 100, 49, 56, 89, 67, 76]
jejum = ['S', 'N', 'S', 'N', 'S', 'N', 'S', 'N', 'S', 'N']
aptos = 0
nao_aptos = 0
for i in range(10):
    idade = idades[i]
    peso = pesos[i]
    esta_em_jejum = jejum[i]
    print('\n'"Usuário: cod.", i,";","Idade:",idade,";","anos","Peso:",peso,"kg","Jejum: ",esta_em_jejum,";")

    if ((18 <= idade <= 67) and (peso > 50) and (esta_em_jejum == esta_em_jejum.upper())):
        if jejum[i] == 'S':
            print("Pode doar sangue")
            aptos += 1

    else:
        print("Não pode doar sangue")
        nao_aptos += 1

print("\nResumo:")
print("Total de doadores aptos: ", aptos)
print("Total de doadores nao aptos: ", nao_aptos)


