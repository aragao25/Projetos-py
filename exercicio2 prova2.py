personagem = input("Informe o nome do personagem: ").upper()
filme = int(input("Informe o número do filme de 1 a 8: "))

personagens = {"HARRY POTTER":1, "HERMIONE GRANGER":1, "RON WEASLEY":1, "ALBUS DUMBLEDORE":1, "SEVERUS SNAPE":1, "RUBEUS HAGRID":1, "DRACO MALFOY":1, "MINERVA MCGONAGALL":1, "LORD VOLDEMORT":1,"DOBBY":2, "GILDEROY":2, "LOCKHART":2, "LUCIUS":2, "MALFOY":2,"SIRIUS BLACK":3, "REMUS LUPIN":3, "PETER PETTIGREW":3,"ALASTOR MOODY":4, "VIKTOR KRUM":4, "FLEUR DELACOUR":4, "BARTY CROUTH JR":4,"DOLORES UMBRIDGE":5, "LUNA LOVEGOOD":5, "BELLATRIX LESTRANGE":5, "NYMPHADORA TONKS":5,"HORACE SLUGHORN":6, "FENRIR GREYBACK":6,"XENOPHILIUS LOVEGOOD":7,"ABERFORTH DUMBLEDORE":8}

if personagem in personagens:
    primeira_vez_que_aparece = personagens[personagem]

    if filme > primeira_vez_que_aparece:
        print(primeira_vez_que_aparece)
    elif filme <= primeira_vez_que_aparece:
        print("DESCONHECIDO")
else:
    print("DESCONHECIDO")