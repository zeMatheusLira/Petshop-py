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

from fpdf import FPDF 

def gerar_relatorio():

    with open("relatorio.txt", "w", encoding="utf-8") as f:
        f.write("=== Relatório do Petshop ===\n")
        
        
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

        
        try:
            caminho_produtos = os.path.join("dados", "produtos.json")
            with open(caminho_produtos, "r", encoding="utf-8") as file:
                produtos = json.load(file)
                f.write("\nProdutos em Estoque:\n")
                for produto in produtos:
                    f.write(f"Produto: {produto['nome']} - Preço: R${produto['preco']:.2f} - Quantidade: {produto['quantidade']}\n")
        except (FileNotFoundError, json.JSONDecodeError):
            f.write("Nenhum produto cadastrado.\n")
    
    print("Relatório TXT gerado com sucesso! Consulte o arquivo 'relatorio.txt'.")

    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    
    pdf.cell(200, 10, txt="=== Relatório do Petshop ===", ln=True, align="C")

    
    pdf.cell(200, 10, txt="Clientes e Pets:", ln=True, align="L")
    try:
        caminho_clientes = os.path.join("dados", "clientes.json")
        with open(caminho_clientes, "r", encoding="utf-8") as file:
            clientes = json.load(file)
            for cliente in clientes:
                pdf.cell(200, 10, txt=f"Cliente: {cliente['nome']} - Telefone: {cliente['telefone']}", ln=True, align="L")
                pdf.cell(200, 10, txt=f"Pet: {cliente['pet']['nome']} - Espécie: {cliente['pet']['especie']}", ln=True, align="L")
    except (FileNotFoundError, json.JSONDecodeError):
        pdf.cell(200, 10, txt="Nenhum cliente cadastrado.", ln=True, align="L")

    
    pdf.cell(200, 10, txt="Produtos em Estoque:", ln=True, align="L")
    try:
        caminho_produtos = os.path.join("dados", "produtos.json")
        with open(caminho_produtos, "r", encoding="utf-8") as file:
            produtos = json.load(file)
            for produto in produtos:
                pdf.cell(200, 10, txt=f"Produto: {produto['nome']} - Preço: R${produto['preco']:.2f} - Quantidade: {produto['quantidade']}", ln=True, align="L")
    except (FileNotFoundError, json.JSONDecodeError):
        pdf.cell(200, 10, txt="Nenhum produto cadastrado.", ln=True, align="L")

    
    pdf.output("relatorio.pdf")
    print("Relatório PDF gerado com sucesso! Consulte o arquivo 'relatorio.pdf'.")

if __name__ == "__main__":
    menu()