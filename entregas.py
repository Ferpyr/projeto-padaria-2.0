from conexao import conectar
def cadastrar_entrega(email, carrinho):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id_cliente FROM clientes WHERE email = %s",
        (email,)
    )

    cliente = cursor.fetchone()
    if not cliente or not carrinho:
        cursor.close()
        conexao.close()
        return False
    id_cliente = cliente[0]
    produtos = []
    valor_total = 0
    for id_produto, quantidade in carrinho.items():
        cursor.execute("""
            SELECT preco
            FROM produtos
            WHERE id_produto = %s
        """, (id_produto,))
        produto = cursor.fetchone()
        if not produto:
            cursor.close()
            conexao.close()
            return False
        subtotal = float(produto[0]) * quantidade
        produtos.append((int(id_produto), quantidade, subtotal))
        valor_total += subtotal
    cursor.execute(
        "SELECT COALESCE(MAX(id_pedido), 0) + 1 FROM pedidos"
    )
    id_pedido = cursor.fetchone()[0]
    cursor.execute("""
        INSERT INTO pedidos
        (id_pedido, id_cliente, status, valor)
        VALUES (%s, %s, %s, %s)
    """, (id_pedido, id_cliente, 'Pendente', valor_total))

    for id_produto, quantidade, subtotal in produtos:
        cursor.execute(
            "SELECT COALESCE(MAX(id_item), 0) + 1 FROM itens_pedido"
        )

        id_item = cursor.fetchone()[0]
        cursor.execute("""
            INSERT INTO itens_pedido
            (id_item, id_produto, id_pedido, quantidade, total)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            id_item,
            id_produto,
            id_pedido,
            quantidade,
            subtotal
        ))
    cursor.execute(
        "SELECT COALESCE(MAX(id_entrega), 0) + 1 FROM entregas"
    )

    id_entrega = cursor.fetchone()[0]
    cursor.execute("""
        INSERT INTO entregas
        (id_entrega, id_pedido, entrega, status, taxa)
        VALUES (%s, %s, NOW(), %s, %s)
    """, (id_entrega, id_pedido, 'Pendente', 0))
    conexao.commit()
    cursor.close()
    conexao.close()
    return id_pedido
