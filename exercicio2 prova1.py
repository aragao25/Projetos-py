
entrada = input().upper().split(";")
cliente, leitura_inicial, leitura_final, dias, poder_calorico, tarifa_kwh, taxa_pct = (entrada)

leitura_inicial1 = int(leitura_inicial)
leitura_final1 = int(leitura_final)
dias1 = int(dias)
poder_calorico1 = float(poder_calorico)
tarifa_kwh1 = float(tarifa_kwh)
taxa_pct1 = float(taxa_pct)

consumo_m3 = leitura_final1 - leitura_inicial1
medias =consumo_m3 / dias1
consumo_kwh = consumo_m3 * poder_calorico1
energia = consumo_kwh * tarifa_kwh1
taxa_val = energia * (taxa_pct1 / 100)
total = energia + taxa_val
m3_dia = consumo_m3 / dias1
kwh_dia = consumo_kwh / dias1

print("RESUMO: CLIENTE", (cliente))
print(f"MEDIDOR: INICIAL={leitura_inicial1:.2f} FINAL={leitura_final1:.2f} DIAS={dias1}")
print(f"CONSUMO: M3={consumo_m3:.2f} KWH={consumo_kwh:.2f}")
print(f"MEDIAS: M3_DIA={m3_dia:.2f} KWH={kwh_dia:.2f}")
print(f"TARIFACAO: TARIFA_KWH=R${tarifa_kwh1:.2f} ENERGIA=R${energia:.2f}")
print(f"TAXA_PCT={taxa_pct1:.2f}% VALOR_TAXA={taxa_val:.2f}")
print(f"TOTAL: {total:.2f}")
if consumo_m3 > 0.0:
    print("CONSUMO_POSITIVO: True")
