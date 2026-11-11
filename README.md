
# Sistema de Padaria - Versão 2.0

## Sobre o Projeto

O Sistema de Gerenciamento de Padaria 2.0 é um projeto desenvolvido com o objetivo de organizar e facilitar o gerenciamento das operações de uma padaria, permitindo o controle de clientes, categorias, produtos, pedidos, pagamentos e entregas.

O projeto utiliza um banco de dados relacional desenvolvido em PostgreSQL, garantindo a organização, integridade e o relacionamento entre as informações.

## Funcionalidades

- **Gerenciamento de Clientes:** cadastro e armazenamento de informações dos clientes, como nome, e-mail, telefone, cidade, estado, CEP e data de nascimento.
- **Gerenciamento de Categorias:** organização dos produtos por categorias.
- **Gerenciamento de Produtos:** cadastro de produtos com nome, descrição, preço, categoria e controle de estoque.
- **Gerenciamento de Pedidos:** registro de pedidos vinculados aos clientes, com data, valor e status.
- **Gerenciamento de Pagamentos:** controle das formas de pagamento, valores, datas e status dos pagamentos.
- **Gerenciamento de Entregas:** acompanhamento das entregas, incluindo horários de saída e entrega, status e taxa.
- **Itens do Pedido:** registro dos produtos, quantidades e valores correspondentes a cada pedido.

## Banco de Dados

O projeto utiliza o PostgreSQL como sistema gerenciador de banco de dados.

### Estrutura das Tabelas

O banco de dados é composto por 7 tabelas principais:

- **clientes:** armazena os dados dos clientes.
- **categoria:** armazena as categorias dos produtos.
- **produtos:** armazena os produtos e seus estoques.
- **pedidos:** registra os pedidos realizados pelos clientes.
- **pagamentos:** registra os pagamentos dos pedidos.
- **entregas:** armazena as informações de entrega dos pedidos.
- **itens_pedido:** armazena os produtos que fazem parte de cada pedido.

### Relacionamentos

- Um cliente pode realizar vários pedidos.
- Uma categoria pode possuir vários produtos.
- Um produto pode estar presente em vários itens de pedidos.
- Um pedido pode possuir vários itens.
- Um pedido pode possuir registros de pagamento.
- Um pedido pode possuir informações de entrega.

## Tecnologias Utilizadas

- **PostgreSQL:** gerenciamento e armazenamento dos dados.
- **SQL:** criação e manipulação das tabelas e relacionamentos.
- **Banco de Dados Relacional:** organização das informações por meio de chaves primárias e estrangeiras.

## Objetivo da Versão 2.0

A versão 2.0 tem como objetivo apresentar uma estrutura de banco de dados mais organizada para o gerenciamento de uma padaria, contemplando diferentes etapas do processo comercial, desde o cadastro de clientes e produtos até o registro de pedidos, pagamentos e entregas.

A estrutura permite centralizar as informações e facilitar futuras implementações e melhorias no sistema.

## Status do Projeto

**Versão:** 2.0

**Status:** Em desenvolvimento.

Desenvolvido como projeto de gerenciamento de dados para uma padaria.
