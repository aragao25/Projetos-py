entrada = input("Digite uma frase: ").split()
nome_conpetidor = " ".join(entrada[1:2]).replace("_", " ").upper()
idade = int(entrada[0])
peso = float(entrada[2])
categoria = (entrada[3]).upper()
print(categoria)

#Processamento
try:
    if ((40.00 <= peso <= 60.00) and (14 <= idade < 16)):
        print(f"NOME={nome_conpetidor}")
        print("INSCRICAO=ACEITA")
    elif (60.01 <= peso <= 80.00) and (16 <= idade < 18):
        print(f"NOME={nome_conpetidor}")
        print("INSCRICAO=ACEITA")
    elif ((80.01 <= peso <= 120.00) and (18 <= idade)):
        print(f"NOME={nome_conpetidor}")
        print("INSCRICAO=ACEITA")

    else:
        if (idade < 14):
            print(f"NOME={nome_conpetidor}")
            print("INSCRICAO=NEGADA: IDADE NAO PERMITIDA")
        else:
            raise ValueError
except:
    print(f"NOME={nome_conpetidor}\n INSCRICAO=NEGADA: PESO E IDADE FORA DOS LIMITES PERMITIDOS")