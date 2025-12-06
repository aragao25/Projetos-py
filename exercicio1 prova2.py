valor_hora_trab = float(input("Digite o valor da hora trabalhada: "))
quant_trab = int(input("Digite a quantidade de horas trabalhadas: "))


sal_bruto = valor_hora_trab * quant_trab
ir = sal_bruto * 0.11
inss = sal_bruto * 0.08
sindicato = sal_bruto * 0.05
salario_liq = sal_bruto - (ir + inss + sindicato)

print(f"+ Salário Bruto : R$ {sal_bruto:.2f}")
print(f"- IR (11%) : R$ {ir:.2f}")
print(f"- INSS (8%) : R$ {inss:.2f}")
print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
print(f"= Salário Líquido : R$ {salario_liq:.2f}")