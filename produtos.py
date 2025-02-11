from utils import carregar_dados, salvar_dados

class Produto:
    @staticmethod
    def menu():
        while True:
            print("\n=== Gerenciar Produtos ===")
            print("1. Cadastrar Produto")
            print("2. Listar Produtos")
            print("3. Atualizar Produto")
            print("4. Remover Produto")
            print("5. Voltar")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                Produto.cadastrar()
            elif opcao == "2":
                Produto.listar()
            elif opcao == "3":
                Produto.atualizar()
            elif opcao == "4":
                Produto.remover()
            elif opcao == "5":
                break
            else:
                print("Opção inválida! Tente novamente.")
    
    @staticmethod
    def cadastrar():
        nome = input("Nome do Produto: ").strip()
        try:
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade em estoque: "))
        except ValueError:
            print("Erro: Preço e quantidade devem ser números válidos.")
            return
        
        produtos = carregar_dados("produtos.json")
        produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
        salvar_dados("produtos.json", produtos)
        
        print("Produto cadastrado com sucesso!")
    
    @staticmethod
    def listar():
        produtos = carregar_dados("produtos.json")
        if not produtos:
            print("Nenhum produto cadastrado.")
            return
        
        for p in produtos:
            print(f"Produto: {p['nome']} | Preço: R${p['preco']:.2f} | Quantidade: {p['quantidade']}")
    
    @staticmethod
    def atualizar():
        Produto.listar()
        nome_produto = input("Digite o nome do produto para atualizar: ").strip()
        
        produtos = carregar_dados("produtos.json")
        for p in produtos:
            if p["nome"].lower() == nome_produto.lower():
                try:
                    p["preco"] = float(input("Novo preço: "))
                    p["quantidade"] = int(input("Nova quantidade: "))
                except ValueError:
                    print("Erro: Preço e quantidade devem ser números válidos.")
                    return
                salvar_dados("produtos.json", produtos)
                print("Produto atualizado com sucesso!")
                return
        
        print("Produto não encontrado.")
    
    @staticmethod
    def remover():
        Produto.listar()
        nome_produto = input("Digite o nome do produto para remover: ").strip()
        
        produtos = carregar_dados("produtos.json")
        produtos = [p for p in produtos if p["nome"].lower() != nome_produto.lower()]
        salvar_dados("produtos.json", produtos)
        
        print("Produto removido com sucesso!")