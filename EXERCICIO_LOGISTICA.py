pedido_frete = input("Informe o nome do pedido: ").split()
print(pedido_frete)
cod_cliente = int(pedido_frete[0])
tipo_servico = (pedido_frete[1]).upper()
regiao_destino = (pedido_frete[2]).upper()
peso = float((pedido_frete[3]).replace(",", "."))

tabela_precos = {"SUL": 5, "SUDESTE":6, "CENTROOESTE":7, "NORTE":8.5, "NORDESTE":8}
servicos = ["PADRAO", "EXPRESSO"]

#verifica se peso é inválido
if peso <= 0:
    print(f"CLIENTE {cod_cliente} PEDIDO NAO ACEITO PESO_INVALIDO")

#verifica limitações
elif (tipo_servico == "EXPRESSO") and (regiao_destino == "NORDESTE" or regiao_destino == "NORTE") and (peso > 30):
    print(f"CLIENTE {cod_cliente} PEDIDO NAO ACEITO PESO_ACIMA_DO_LIMITE")
elif ((tipo_servico == "PADRAO") or tipo_servico == "EXPRESSO") and (peso > 100):
    print(f"CLIENTE {cod_cliente} PEDIDO NAO ACEITO PESO_ACIMA_DO_LIMITE")

#calculo do frete
elif regiao_destino in tabela_precos:
    preco_base = tabela_precos[regiao_destino]
    if tipo_servico == "PADRAO":
        valor = preco_base * peso
        print(f"CLIENTE {cod_cliente} SERVICO {servicos[0]} REGIAO {regiao_destino} TOTAL R$ {valor:.2f}")
    elif tipo_servico == "EXPRESSO":
        valor = (preco_base * peso) * 1.5
        print(f"CLIENTE {cod_cliente} SERVICO {servicos[1]} REGIAO {regiao_destino} TOTAL R$ {valor:.2f}")
else:
    print("FIM")




