from utils import carregar_dados, salvar_dados

class Servico:
    @staticmethod
    def menu():
        while True:
            print("\n=== Gerenciar Serviços ===")
            print("1. Agendar Serviço")
            print("2. Listar Serviços Agendados")
            print("3. Remover Serviço")
            print("4. Voltar")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                Servico.agendar()
            elif opcao == "2":
                Servico.listar()
            elif opcao == "3":
                Servico.remover()
            elif opcao == "4":
                break
            else:
                print("Opção inválida! Tente novamente.")
    
    @staticmethod
    def agendar():
        cliente = input("Nome do Cliente: ").strip()
        pet = input("Nome do Pet: ").strip()
        servico = input("Serviço desejado: ").strip()
        data = input("Data do serviço (DD/MM/AAAA): ").strip()
        
        agendamentos = carregar_dados("servicos.json")
        agendamentos.append({"cliente": cliente, "pet": pet, "servico": servico, "data": data})
        salvar_dados("servicos.json", agendamentos)
        
        print("Serviço agendado com sucesso!")
    
    @staticmethod
    def listar():
        agendamentos = carregar_dados("servicos.json")
        if not agendamentos:
            print("Nenhum serviço agendado.")
            return
        
        for ag in agendamentos:
            print(f"Cliente: {ag['cliente']} | Pet: {ag['pet']} | Serviço: {ag['servico']} | Data: {ag['data']}")
    
    @staticmethod
    def remover():
        Servico.listar()
        nome_cliente = input("Digite o nome do cliente para remover o agendamento: ").strip()
        
        agendamentos = carregar_dados("servicos.json")
        agendamentos = [ag for ag in agendamentos if ag["cliente"].lower() != nome_cliente.lower()]
        salvar_dados("servicos.json", agendamentos)
        
        print("Agendamento removido com sucesso!")