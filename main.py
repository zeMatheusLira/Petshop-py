import json
import os
from cliente import Cliente
from servicos import Servico
from produtos import Produto

def menu():
    while True:
        print("\n=== Sistema de Petshop ===")
        print("1. Gerenciar Clientes e Pets")
        print("2. Agendar Serviços")
        print("3. Gerenciar Produtos")
        print("4. Gerar Relatório")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            Cliente.menu()
        elif opcao == "2":
            Servico.menu()
        elif opcao == "3":
            Produto.menu()
        elif opcao == "4":
            gerar_relatorio()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def gerar_relatorio():
    with open("./report/relatorio.txt", "w", encoding="utf-8") as f:
        f.write("=== Relatório do Petshop ===\n")
        
        # Relatório de Clientes
        try:
            caminho_clientes = os.path.join("dados", "clientes.json")
            with open(caminho_clientes, "r", encoding="utf-8") as file:
                clientes = json.load(file)
                f.write("\nClientes e Pets:\n")
                for cliente in clientes:
                    f.write(f"Cliente: {cliente['nome']} - Telefone: {cliente['telefone']}\n")
                    f.write(f"Pet: {cliente['pet']['nome']} - Espécie: {cliente['pet']['especie']}\n")
        except (FileNotFoundError, json.JSONDecodeError):
            f.write("Nenhum cliente cadastrado.\n")

        # Relatório de Produtos
        try:
            caminho_produtos = os.path.join("dados", "produtos.json")
            with open(caminho_produtos, "r", encoding="utf-8") as file:
                produtos = json.load(file)
                f.write("\nProdutos em Estoque:\n")
                for produto in produtos:
                    f.write(f"Produto: {produto['nome']} - Preço: R${produto['preco']:.2f} - Quantidade: {produto['quantidade']}\n")
        except (FileNotFoundError, json.JSONDecodeError):
            f.write("Nenhum produto cadastrado.\n")
    
    print("Relatório gerado com sucesso! Consulte o arquivo 'relatorio.txt'.")

if __name__ == "__main__":
    menu()