# Inicialização dos vetores (listas) para armazenar os dados
nomes_completos = []
notas_alunos = []

print("--- Sistema de Gerenciamento Escolar ---")

while True:
    # Interface de Usuário - Menu
    print("\nMENU DE OPÇÕES:")
    print("1 - Cadastro de Alunos")
    print("2 - Informações de Alunos")
    print("3 - Modificar nota")
    print("4 - Média de notas")
    print("0 - Sair")

    opcao = input("Escolha uma funcionalidade: ")

    # F.1 - Cadastro de Alunos
    if opcao == '1':
        nome_do_aluno = input("Digite o nome do aluno: ")
        resultado_nome = nome_do_aluno.strip().upper()

        sobrenome = input("Digite o sobrenome do aluno: ")
        resultado_sobrenome = sobrenome.strip().upper()

        # Validação da nota conforme sua lógica de conversão
        while True:
            nota_input = input("Digite a nota do aluno (0 a 10): ").strip().replace(',', '.')
            try:
                nota = float(nota_input)
                if 0 <= nota <= 10:
                    break
                else:
                    print("Erro: A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Erro ao ler nota do aluno. Nota não é um número válido!")

        # Armazenamento nos vetores
        nomes_completos.append(resultado_nome + ' ' + resultado_sobrenome)
        notas_alunos.append(nota)
        print(f"Aluno cadastrado! Matrícula: {len(nomes_completos) - 1}")

    # F.2 – Informações de Alunos
    elif opcao == '2':
        if not nomes_completos:
            print("Aviso: Não existem alunos cadastrados no sistema.")
        else:
            print("\n--- LISTA DE ALUNOS ---")
            # Uso de FOR para lidar com vetor
            for i in range(len(nomes_completos)):
                print(f"Matrícula: {i} | Nome: {nomes_completos[i]} | Nota: {notas_alunos[i]}")

    # F.3 – Modificar nota
    elif opcao == '3':
        if not nomes_completos:
            print("Erro: Não existe aluno no sistema.")
        else:
            try:
                matricula = int(input("Digite o número de matrícula para modificar a nota: "))

                # Verifica se a matrícula (posição) existe no vetor
                if 0 <= matricula < len(nomes_completos):
                    while True:
                        nova_nota_input = input(f"Digite a nova nota para {nomes_completos[matricula]}: ").replace(',',
                                                                                                                   '.')
                        nova_nota = float(nova_nota_input)
                        if 0 <= nova_nota <= 10:
                            notas_alunos[matricula] = nova_nota
                            print("Nota atualizada com sucesso!")
                            break
                        else:
                            print("Erro: Nota deve ser entre 0 e 10.")
                else:
                    print("Erro: O número da matrícula não existe.")
            except ValueError:
                print("Erro: Digite um número inteiro para a matrícula.")

    # F.4 – Média de notas
    elif opcao == '4':
        if not notas_alunos:
            print("Aviso: Não há alunos para calcular a média.")
        else:
            soma = 0
            for n in notas_alunos:
                soma += n
            media = soma / len(notas_alunos)
            print(f"A média de notas da turma é: {media:.22f}")  # Exibe a média com precisão

    # F.0 - Sair
    elif opcao == '0':
        print("O sistema foi fechado.")
        break

    # Desconsiderar qualquer valor diferente do menu
    else:
        continue