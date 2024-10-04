import pandas as pd
import os

# Função para carregar dados de um arquivo CSV (se existir)
def carregar_dados(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        return df.to_dict('records')
    except FileNotFoundError:
        return []

# Função para salvar dados em um arquivo CSV
def salvar_dados(dados, nome_arquivo):
    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False)


# Função para consultar o estoque
def consultar_estoque(produtos):
    if not produtos:
        print("Não há produtos cadastrados.")
    else:
        print("\nProdutos em Estoque:")
        for produto in produtos:
            valor_estoque = produto['quantidade'] * produto['preco']
            print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Valor em Estoque: R$ {valor_estoque:.2f}")

# Conjunto para armazenar códigos únicos
codigos_cadastrados = set()

# Inicialização
produtos = carregar_dados('produtos.csv')
vendas = carregar_dados('vendas.csv')

# Preencher o conjunto com os códigos já existentes
for produto in produtos:
    codigos_cadastrados.add(produto['codigo'])

while True:
    print("1. Cadastrar Produto")
    print("2. Registrar Venda")
    print("3. Gerar Relatório de Vendas")
    print("4. Gerar Relatório de Estoque")
    print("5. Consultar Estoque")  # Nova opção
    print("6. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        codigo = input("Código do produto: ")
        # Verifica se o código já existe
        while codigo in codigos_cadastrados:
            print("Código já cadastrado. Informe um novo código:")
            codigo = input("Código do produto: ")
        # Se o código for novo, adiciona ao conjunto e à lista de produtos
        codigos_cadastrados.add(codigo)
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade em estoque: "))
        preco = float(input("Preço por unidade: "))
        produto = {'codigo': codigo, 'nome': nome, 'quantidade': quantidade, 'preco': preco}
        produtos.append(produto)
        salvar_dados(produtos, 'produtos.csv')
    elif opcao == 2:
        codigo = input("Código do produto: ")
        quantidade_vendida = int(input("Quantidade vendida: "))
        for produto in produtos:
            if produto['codigo'] == codigo:
                if produto['quantidade'] >= quantidade_vendida:
                    produto['quantidade'] -= quantidade_vendida
                    venda = {'codigo': codigo, 'quantidade': quantidade_vendida, 'valor_total': quantidade_vendida * produto['preco']}
                    vendas.append(venda)
                    salvar_dados(produtos, 'produtos.csv')
                    salvar_dados(vendas, 'vendas.csv')
                    print("Venda registrada com sucesso!")
                else:
                    print("Quantidade em estoque insuficiente.")
                break
        else:
            print("Produto não encontrado.")
    elif opcao == 3:
            diretorio = input("Informe o diretório para salvar o relatório de vendas: ")
            nome_arquivo = os.path.join(diretorio, 'relatorio_vendas.csv')
            df = pd.DataFrame(vendas)
            df.to_csv(nome_arquivo, index=False)
            print(f"Relatório de vendas gerado com sucesso em {nome_arquivo}!")

    elif opcao == 4:
        diretorio = input("Informe o diretório para salvar o relatório de estoque: ")
        nome_arquivo = os.path.join(diretorio, 'relatorio_estoque.txt')
        with open(nome_arquivo, 'w') as arquivo:
            for produto in produtos:
                arquivo.write(
                    f"Código: {produto['codigo']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}\n")
        print(f"Relatório de estoque gerado com sucesso em {nome_arquivo}!")

    elif opcao == 5:
        consultar_estoque(produtos)

    elif opcao == 6:
        break
    else:
        print("Opção inválida.")