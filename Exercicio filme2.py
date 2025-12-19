

dicionario_personagem = {
    "1": ["HARRY POTTER", "HERMIONE GRANGER", "RON WEASLEY", "ALBUS DUMBLEDORE", "SEVERO SNAPE", "RUBEUS HAGRID", "DRACO MALFOY", "MINERVA MCGONAGALL", "LORD VOLDEMORT"],
    "2": ["DOBBY", "GILDEROY LOCKHART", "LUCIUS MALFOY"],
    "3": ["SIRIUS BLACK", "REMUS LUPIN", "PETER PETTIGREW"],
    "4": ["ALASTOR MOODY", "VIKTOR KRUM", "FLEUR DELACOUR", "BARTY CROUCH JR"],
    "5": ["DOLORES UMBRIDGE", "LUNA LOVEGOOD", "BELLATRIX LESTRANGE", "NYMPHADORA TONKS"],
    "6": ["HORACE SLUGHORN", "FENRIR GREYBACK"],
    "7": ["XENOPHILIUS LOVEGOOD"],
    "8": ["ALBERFORTH DUMBLEDORE"]
}
apareceu_antes = False


entrada = input().replace("_", " ").upper().split()
filme_pesquisado = int(entrada[0])
nome_personagem = " ".join(entrada[1:])
for numero_filme_str_chaves, lista_personagem_valores_dic in dicionario_personagem.items():
    numero_filme_atual = int(numero_filme_str_chaves)
    if nome_personagem in lista_personagem_valores_dic:
        if numero_filme_atual < filme_pesquisado:
            apareceu_antes = True
if apareceu_antes:
    print("CONHECIDO")
else:
    print("DESCONHECIDO")



