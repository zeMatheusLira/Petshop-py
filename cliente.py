from utils import carregar_dados, salvar_dados

class Cliente:
    @staticmethod
    def menu():
        while True:
            print("\n=== Gerenciar Clientes e Pets ===")
            print("1. Cadastrar Cliente e Pet")
            print("2. Listar Clientes e Pets")
            print("3. Atualizar Cliente")
            print("4. Remover Cliente")
            print("5. Voltar")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                Cliente.cadastrar()
            elif opcao == "2":
                Cliente.listar()
            elif opcao == "3":
                Cliente.atualizar()
            elif opcao == "4":
                Cliente.remover()
            elif opcao == "5":
                break
            else:
                print("Opção inválida! Tente novamente.")
    
    @staticmethod
    def cadastrar():
        nome = input("Nome do Cliente: ").strip()
        telefone = input("Telefone: ").strip()
        pet_nome = input("Nome do Pet: ").strip()
        pet_especie = input("Espécie do Pet: ").strip()
        
        if not nome or not telefone or not pet_nome or not pet_especie:
            print("Erro: Nenhum campo pode estar vazio.")
            return
        
        cliente = {"nome": nome, "telefone": telefone, "pet": {"nome": pet_nome, "especie": pet_especie}}
        
        clientes = carregar_dados("clientes.json")
        clientes.append(cliente)
        salvar_dados("clientes.json", clientes)
        
        print("Cliente e pet cadastrados com sucesso!")
    
    @staticmethod
    def listar():
        clientes = carregar_dados("clientes.json")
        if not clientes:
            print("Nenhum cliente cadastrado ainda.")
            return
        
        for cliente in clientes:
            print(f"Cliente: {cliente['nome']} - Telefone: {cliente['telefone']}")
            print(f"Pet: {cliente['pet']['nome']} - Espécie: {cliente['pet']['especie']}")
    
    @staticmethod
    def atualizar():
        Cliente.listar()
        nome_cliente = input("Digite o nome do cliente que deseja atualizar: ").strip()
        
        clientes = carregar_dados("clientes.json")
        for cliente in clientes:
            if cliente["nome"].lower() == nome_cliente.lower():
                cliente["telefone"] = input("Novo telefone: ").strip()
                cliente["pet"]["nome"] = input("Novo nome do pet: ").strip()
                cliente["pet"]["especie"] = input("Nova espécie do pet: ").strip()
                salvar_dados("clientes.json", clientes)
                print("Cliente atualizado com sucesso!")
                return
        
        print("Cliente não encontrado.")
    
    @staticmethod
    def remover():
        Cliente.listar()
        nome_cliente = input("Digite o nome do cliente que deseja remover: ").strip()
        
        clientes = carregar_dados("clientes.json")
        clientes = [c for c in clientes if c["nome"].lower() != nome_cliente.lower()]
        salvar_dados("clientes.json", clientes)
        
        print("Cliente removido com sucesso!")