quant_planos = int(input("Quantidade de planos: "))

for x in range(quant_planos):
    try:
        # Nota: Corrigi o input() que estava com o .split() no lugar errado
        entrada = input(f"Digite os dados do plano {x + 1}: ")
        plano = entrada.split()

        cod_cliente = int(plano[0])
        valor_energetico = int(plano[1])
        porcao_frutas = int(plano[2])
        verd_legumes = int(plano[3])
        processados = int(plano[4])

        # 1. Criamos uma lista vazia para armazenar as falhas
        falhas = []

        # 2. Verificamos cada condição individualmente
        if not (1500 <= valor_energetico <= 2500):
            falhas.append("caloria_fora_faixa")

        if porcao_frutas < 2:
            falhas.append("frutas_insuficientes")

        if verd_legumes < 3:
            falhas.append("verduras_insuficientes")

        if processados > 20:
            falhas.append("ultraprocessados_excessivos")

        # 3. Lógica de decisão baseada na quantidade de falhas
        if len(falhas) == 0:
            print(f"PACIENTE {cod_cliente} PLANO APROVADO")
        elif len(falhas) == 1:
            # Se só tem 1 item na lista, mostramos esse item específico
            print(f"PACIENTE {cod_cliente} REPROVADO: {falhas[0]}")
        else:
            # Se tem mais de 1, mostramos a mensagem genérica
            print(f"PACIENTE {cod_cliente} REPROVADO: multiplos_criterios")

    except ValueError:
        print("Erro: Certifique-se de digitar apenas números inteiros.")
    except IndexError:
        print("Erro: Você não digitou todos os 5 valores necessários.")

