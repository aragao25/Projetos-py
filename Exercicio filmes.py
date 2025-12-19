entrada = input()
nome_filme = entrada.replace("_", " ").split()

try:
    # 1. Validação de Estrutura
    if len(nome_filme) < 8:
        raise ValueError

    # 2. Extração e Conversão (Gera ValueError se nota ou idade não forem números)
    filme1 = " ".join(nome_filme[0:4]).upper()
    tipo_versao = nome_filme[4].upper()
    idioma = nome_filme[5].upper()
    nota = float(nome_filme[6].replace(",", "."))
    idade = int(nome_filme[7])

    # 3. Validação de Regras (DADOS INVÁLIDOS)
    if idioma not in ["EN", "PT-BR"]:
        raise ValueError
    if not (0 <= nota <= 10): # Exemplo: nota deve ser entre 0 e 10
        raise ValueError
    if tipo_versao not in ["EXTENDIDA", "CINEMA"]:
        raise ValueError

    # --- Se chegou aqui, todos os dados são válidos. Começam os prints ---

    print(f"TITULO={filme1}")

    # Áudio
    if idioma == "EN":
        print("AUDIO: LEGENDADO")
    else:
        print("AUDIO: DUBLADO")

    # Permissão
    if idade >= 0: # Ajuste a idade conforme a regra do seu exercício
        print("PERMISSAO: PERMITIDO")
    else:
        print("PERMISSAO: PROIBIDO")

    # Selo
    if (tipo_versao == "EXTENDIDA" or tipo_versao == "CINEMA") and nota >= 8:
        print("SELO: OBRIGATÓRIO")
    elif nota >= 7:
        print("SELO: RECOMENDADO")
    else:
        print("SELO: OPCIONAL")

except:
    print("DADOS INVÁLIDOS")