<p><img src="/Imagem/UNIATENEU.png"></p>

# Trabalho Prático - Sistema de Controle de Vendas
- Objetivo:
Desenvolver um programa em Python que simule um sistema simples de controle de vendas para uma loja. O sistema deverá ser capaz de cadastrar produtos, registrar vendas e gerar relatórios de vendas com base nos dados manipulados.

- Descrição do Problema:
Você foi contratado para desenvolver um sistema que ajude uma pequena loja a organizar seus produtos e vendas.

O sistema deve permitir as seguintes funcionalidades:
1. Cadastrar Produtos:
O programa deve permitir ao usuário cadastrar novos produtos com as seguintes informações:
- Código do produto (string)
- Nome do produto (string)
- Quantidade em estoque (inteiro)
- Preço por unidade (float)
2. Registrar Venda:
O programa deve registrar a venda de um ou mais produtos. Para isso, o sistema deve solicitar ao usuário:
- Código do produto
- Quantidade vendida
- O sistema deve verificar se há quantidade suficiente no estoque para realizar a venda. Caso positivo, a venda é registrada e a quantidade em estoque é atualizada.

3. Relatório de Vendas (geração de arquivo CSV):
O programa deve gerar um relatório em formato CSV com as vendas realizadas, contendo:
- Código do produto
- Nome do produto
- Quantidade vendida
- Valor total da venda (quantidade vendida * preço por unidade)
- Esse relatório deve ser salvo em um arquivo CSV que possa ser aberto posteriormente para análise.

4. Relatório de Estoque (geração de arquivo de texto):
O sistema deve permitir que o usuário gere um relatório simples em um arquivo de texto (.txt) com a lista dos produtos e suas quantidades em estoque. O relatório deve conter:
- Código do produto
- Nome do produto
- Quantidade em estoque

5 Requisitos Técnicos:
- O programa deve utilizar estruturas de dados como listas, dicionários e tuplas para armazenar as informações dos produtos e das vendas.
- Utilizar a biblioteca pandas para gerar e manipular o arquivo CSV de vendas.
- O sistema deve ser capaz de lidar com entradas de dados inválidas (por exemplo, tentar vender mais produtos do que há no estoque).
- Ao reiniciar o programa, os dados dos produtos cadastrados e das vendas devem ser carregados corretamente dos arquivos gerados anteriormente (se houver).