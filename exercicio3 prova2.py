entrada = input().upper().split(";")
cliente, gb_consumidos, tarifa_gb, taxa_servico_pct, desconto_fidelidade_pct, bonus_gb = entrada

gb_consumidos = float(gb_consumidos)
tarifa_gb = float(tarifa_gb)
taxa_servico_pct = float(taxa_servico_pct)
desconto_fidelidade_pct = float(desconto_fidelidade_pct)
bonus_gb = float(bonus_gb)

consumo_liq = gb_consumidos - bonus_gb
valor_dados = consumo_liq * tarifa_gb
taxa_val = valor_dados * (taxa_servico_pct / 100)
desconto_val = valor_dados * (desconto_fidelidade_pct / 100)
total = valor_dados + taxa_val - desconto_val

bonus_aplic = bool(bonus_gb > 0.0)
fidelidade_aplic = bool(gb_consumidos > 0.0)
consumo_positivo = bool(gb_consumidos > 0.0)

print(f"CONSUMO: {gb_consumidos:.2f} BONUS_GB: {bonus_gb:.2f} LIQ_GB= {consumo_liq:.2f}")
print(f"TARIFACAO: TARIFA_GB=R$ {tarifa_gb:.2f} VALOR_DADOS: {valor_dados:.2f}")
print(f"TAXAS: SERVICO_PCT={taxa_servico_pct:.2f}% VALOR=R${taxa_val:.2f}")
print(f"DESCONTO_FIDELIDADE: {desconto_fidelidade_pct:.2f}% VALOR=R${desconto_val:.2f}")
print(f"TOTAL: {total:.2f}")
print(f"BONUS_APLICADO: {bonus_aplic:.2f} FIDELIDADE_APLICADA: {fidelidade_aplic:.2f} CONSUMO_POSITIVO: {consumo_positivo:.2f}")




