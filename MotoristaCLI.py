from Corrida import Corrida
from Motorista import Motorista
from Passageiro import Passageiro

class GestaoMotorista:
    def __init__(self, motorista_db):
        self.motorista_db = motorista_db

    def exibir_menu(self):
        while True:
            print("\nMenu Principal:")
            print("1. Adicionar Motorista")
            print("2. Consultar Motorista")
            print("3. Editar Motorista")
            print("4. Remover Motorista")
            print("5. Encerrar")

            opcao = input("Selecione uma opção: ")

            if opcao == "1":
                self.adicionar_motorista()
            elif opcao == "2":
                self.consultar_motorista()
            elif opcao == "3":
                self.editar_motorista()
            elif opcao == "4":
                self.remover_motorista()
            elif opcao == "5":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def adicionar_motorista(self):
        avaliacao = int(input("Informe a avaliação do motorista: "))
        nome_passageiro = input("Nome do passageiro: ")
        documento_passageiro = input("Documento do passageiro: ")
        avaliacao_corrida = int(input("Avaliação da corrida: "))
        distancia = float(input("Distância percorrida (km): "))
        valor = float(input("Valor da corrida (R$): "))

        passageiro = Passageiro(nome_passageiro, documento_passageiro)
        corrida = Corrida(avaliacao_corrida, distancia, valor, passageiro)
        motorista = Motorista([corrida], avaliacao)

        self.motorista_db.cadastrar_motorista(motorista)

    def consultar_motorista(self):
        id_motorista = input("Informe o ID do motorista: ")
        motorista = self.motorista_db.buscar_motorista(id_motorista)
        if motorista:
            print("Dados do Motorista:")
            print("Avaliação:", motorista.avaliacao)
            print("Corridas registradas:")
            for corrida in motorista.corridas:
                print(f"  - Avaliação da corrida: {corrida.nota}")
                print(f"    Distância: {corrida.distancia} km")
                print(f"    Valor: R${corrida.valor}")
                print("    Dados do Passageiro:")
                print(f"      Nome: {corrida.passageiro.nome}")
                print(f"      Documento: {corrida.passageiro.documento}")

    def editar_motorista(self):
        id_motorista = input("Informe o ID do motorista para atualização: ")
        nova_avaliacao = int(input("Nova avaliação do motorista: "))
        novo_nome_passageiro = input("Novo nome do passageiro: ")
        novo_documento_passageiro = input("Novo documento do passageiro: ")
        nova_avaliacao_corrida = int(input("Nova avaliação da corrida: "))
        nova_distancia = float(input("Nova distância da corrida: "))
        novo_valor = float(input("Novo valor da corrida: "))

        novo_passageiro = Passageiro(novo_nome_passageiro, novo_documento_passageiro)
        nova_corrida = Corrida(nova_avaliacao_corrida, nova_distancia, novo_valor, novo_passageiro)
        motorista_atualizado = Motorista([nova_corrida], nova_avaliacao)

        self.motorista_db.atualizar_motorista(id_motorista, motorista_atualizado)

    def remover_motorista(self):
        id_motorista = input("Informe o ID do motorista a ser removido: ")
        self.motorista_db.remover_motorista(id_motorista)
