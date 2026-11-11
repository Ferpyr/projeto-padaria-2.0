-- Active: 1788286412804@@127.0.0.1@5432@banco_padaria
CREATE DATABASE banco_padaria;

CREATE TABLE clientes (
    id_cliente INTEGER NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(3) NOT NULL,
    cep VARCHAR(200) NOT NULL,
    data_nascimento DATE NOT NULL,
    senha VARCHAR(30) NOT NULL
);


CREATE TABLE categoria (
    id_categoria INTEGER NOT NULL PRIMARY KEY,
    categoria VARCHAR(50)
);

CREATE TABLE produtos (
    id_produto INTEGER NOT NULL PRIMARY KEY,
    id_categoria INTEGER NOT NULL REFERENCES categoria(id_categoria),
    nome_produto VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    estoque INTEGER NOT NULL
);

CREATE TABLE pedidos (
    id_pedido INTEGER NOT NULL PRIMARY KEY,
    id_cliente INTEGER NOT NULL REFERENCES clientes(id_cliente),
    data TIMESTAMP NOT NULL DEFAULT NOW(),
    status VARCHAR(30) NOT NULL DEFAULT 'Pendente',
    valor DECIMAL(10,2)
);

CREATE TABLE pagamentos (
    id_pagamento INTEGER NOT NULL PRIMARY KEY,
    id_pedido INTEGER NOT NULL REFERENCES pedidos(id_pedido),
    forma_pagamento VARCHAR(30) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'Pendente',
    data TIMESTAMP DEFAULT NOW()
);

CREATE TABLE entregas (
    id_entrega INTEGER NOT NULL PRIMARY KEY,
    id_pedido INTEGER NOT NULL REFERENCES pedidos(id_pedido),
    saida TIMESTAMP NOT NULL DEFAULT NOW(),
    entrega TIMESTAMP NOT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'Pendente',
    taxa DECIMAL(10,2)
);

CREATE TABLE itens_pedido (
    id_item INTEGER NOT NULL PRIMARY KEY,
    id_produto INTEGER NOT NULL REFERENCES produtos(id_produto),
    id_pedido INTEGER NOT NULL REFERENCES pedidos(id_pedido),
    quantidade INTEGER NOT NULL,
    total DECIMAL(10,2)
);
