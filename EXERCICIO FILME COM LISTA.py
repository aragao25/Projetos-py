lista_personagem = [
                ["HARRY POTTER", "HERMIONE GRANGER", "RON WEASLEY", "ALBUS DUMBLEDORE", "SEVERO SNAPE", "RUBEUS HAGRID", "DRACO MALFOY", "MINERVA MCGONAGALL", "LORD VOLDEMORT"],
                ["DOBBY", "GILDEROY LOCKHART", "LUCIUS MALFOY"],
                ["SIRIUS BLACK", "REMUS LUPIN", "PETER PETTIGREW"],
                ["ALASTOR MOODY", "VIKTOR KRUM", "FLEUR DELACOUR", "BARTY CROUCH JR"],
                ["DOLORES UMBRIDGE", "LUNA LOVEGOOD", "BELLATRIX LESTRANGE", "NYMPHADORA TONKS"],
                ["HORACE SLUGHORN", "FENRIR GREYBACK"],
                ["XENOPHILIUS LOVEGOOD"],
                ["ALBERFORTH DUMBLEDORE"]
    ]
apareceu_antes = False

entrada = input().upper().replace("_", " ").split()
print(entrada)

nome_personagem = " ".join(entrada[1:])
print(nome_personagem)
filme_pesquisado = int(entrada[0])
for indice, nome in enumerate(lista_personagem):
    numero_filme = indice + 1
    if nome_personagem in nome:
        if numero_filme < filme_pesquisado:
            apareceu_antes = True

# ou
# for i in range(len(lista_filmes)):
#     # i começa em 0, 1, 2...
#     sublista = lista_filmes[i]
#     numero_filme = i + 1
#
#     if nome_personagem in sublista:
#         if numero_filme < filme_pesquisado:
#             apareceu_antes = True
if apareceu_antes:
    print("CONHECIDO")
else:
    print("DESCONHECIDO")