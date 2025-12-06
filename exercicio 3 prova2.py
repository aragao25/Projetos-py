from statistics import median_low

entrada = input("Inscreva seu competidor: ")

nome_competidor = entrada.upper().split()
nome_norm = nome_competidor[1].replace("_", " ")
idade = int(nome_competidor[0])
peso = float(nome_competidor[2])
categoria = nome_competidor[3]

if (14 <= idade) and (40 <= peso <= 60.00) and (categoria == "LEVE"):
    print("INSCRIÇÃO ACEITA")
elif (16 <= idade) and (60.01 <= peso <= 80.00) and (categoria == "MEDIO"):
    print("INSCRIÇÃO ACEITA")
elif (18 <= idade) and (80.01 <= peso <= 120.00) and (categoria == "PESADO"):
    print("INSCRIÇÃO ACEITA")
elif idade < 14:
    print("INSCRIÇÃO NEGADA: IDADE NÃO PERMITIDA")
elif peso < 40:
    print("INSCRIÇÃO NEGADA: PESO NÃO PERMITIDO")
elif (16 <= idade < 18) and (80.01 <= peso <= 120.00):
    print("INSCRIÇÃO NEGADA: PESO E IDADE FORA DOS LIMITES PERMITIDOS")
else:
    print("INSCRIÇÃO NEGADA: DADOS FORA DOS PADRÕES")