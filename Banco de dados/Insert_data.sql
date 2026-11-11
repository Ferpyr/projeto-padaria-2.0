-- Active: 1788286412804@@127.0.0.1@5432@banco_padaria
INSERT INTO clientes (id_cliente, nome, email, telefone, cidade, estado, cep, data_nascimento, senha)
VALUES
(1, 'João Silva', 'joao@gmail.com', '(11) 99999-1111', 'São Paulo', 'SP', '01001-000', '1995-05-12', 'senha123'),

(2, 'Maria Oliveira', 'maria@gmail.com', '(21) 98888-2222', 'Rio de Janeiro', 'RJ', '20040-002', '1998-08-23', 'maria123'),

(3, 'Pedro Santos', 'pedro@gmail.com', '(31) 97777-3333', 'Belo Horizonte', 'MG', '30130-010', '1990-03-15', 'pedro123'),

(4, 'Ana Costa', 'ana@gmail.com', '(41) 96666-4444', 'Curitiba', 'PR', '80010-000', '2000-11-07', 'ana123'),

(5, 'Lucas Pereira', 'lucas@gmail.com', '(51) 95555-5555', 'Porto Alegre', 'RS', '90010-150', '1997-01-19', 'lucas123'),

(6, 'Juliana Ferreira', 'juliana@gmail.com', '(81) 94444-6666', 'Recife', 'PE', '50010-000', '1996-07-30', 'julia123'),

(7, 'Gabriel Almeida', 'gabriel@gmail.com', '(71) 93333-7777', 'Salvador', 'BA', '40020-000', '1993-09-14', 'gabriel123'),

(8, 'Beatriz Rodrigues', 'beatriz@gmail.com', '(85) 92222-8888', 'Fortaleza', 'CE', '60010-000', '2001-04-25', 'bia123'),

(9, 'Rafael Martins', 'rafael@gmail.com', '(62) 91111-9999', 'Goiânia', 'GO', '74000-000', '1992-12-03', 'rafael123'),

(10, 'Camila Souza', 'camila@gmail.com', '(27) 90000-0000', 'Vitória', 'ES', '29010-000', '1999-06-18', 'camila123');


INSERT INTO categoria (id_categoria, categoria) VALUES
(1, 'Pães'),
(2, 'Salgados'),
(3, 'Doces'),
(4, 'Bebidas');

INSERT INTO produtos
(id_produto, id_categoria, nome_produto, descricao, preco, estoque)
VALUES
(1, 1, 'Pão Francês', 'Crocante por fora e macio por dentro.', 0.80, 100),
(2, 1, 'Croissant', 'Massa folhada e sabor irresistível.', 7.50, 50),
(3, 3, 'Bolo de Chocolate', 'Bolo fofinho com cobertura de chocolate.', 12.00, 20),
(4, 3, 'Sonho', 'Recheado com creme especial.', 6.00, 30),
(5, 2, 'Misto Quente', 'Pão, queijo e presunto.', 9.00, 30),
(6, 1, 'Pão de Queijo', 'Quentinho e cheio de queijo.', 4.00, 50),
(7, 1, 'Pão de Leite', 'Delicioso e nutritivo.', 2.50, 50),
(8, 3, 'Cueca Virada', 'Deliciosa e nutritiva.', 3.50, 30),
(9, 1, 'Pão de Forma', 'Delicioso e nutritivo.', 5.00, 30),
(10, 2, 'Pastel', 'Recheado com carne e queijo.', 12.00, 30),
(11, 2, 'Coxinha', 'Recheada com frango desfiado ou carne moída.', 8.00, 40),
(12, 2, 'Esfirra', 'Recheada com carne e queijo.', 6.00, 30),
(13, 3, 'Pudim', 'Delicioso e cremoso.', 7.00, 20),
(14, 4, 'Café', 'Delicioso e aromático.', 3.00, 100),
(15, 4, 'Sucos Naturais', 'Deliciosos e refrescantes.', 4.00, 50),
(16, 4, 'Cappuccino', 'Delicioso e aromático.', 5.00, 50),
(17, 2, 'Pizza', 'Deliciosa e saborosa.', 5.00, 30);