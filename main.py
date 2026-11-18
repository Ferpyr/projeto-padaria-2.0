from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'somosgueto123'
from conexao import conectar
from usuario import validar_login
from entregas import cadastrar_entrega
@app.route('/')
def inicio():
    return 'dado'
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
@app.route('/fazer_login', methods=['POST'])
def fazer_login():
    email = request.form['email']
    senha = request.form['senha']

    logado = validar_login(email, senha)

    if logado == True:
        return render_template('produtos.html')
    else:
        return render_template('login.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')


@app.route('/fazer_cadastro', methods=['POST'])
def fazer_cadastro():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    cidade = request.form['cidade']
    estado = request.form['estado']
    cep = request.form['cep']
    data_nascimento = request.form['data_nascimento']
    senha = request.form['senha']
    parametros = [
        nome,
        email,
        telefone,
        cidade,
        estado,
        cep,
        data_nascimento,
        senha
    ]
    sql = '''
        INSERT INTO clientes (
            nome, email, telefone, cidade,
            estado, cep, data_nascimento, senha
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect(url_for('login'))

@app.route('/entregas', methods=['GET'])
def entregas():
    return render_template('entregas.html')

@app.route('/fazer_entrega', methods=['POST'])
def fazer_entrega():

    email = request.form['email']
    carrinho = session.get('carrinho', {})
    resultado = cadastrar_entrega(email, carrinho)
    if resultado:
        session.pop('carrinho', None)
        return redirect(
            url_for('pagamento', id_pedido=resultado)
        )
    return redirect(url_for('carrinho'))

@app.route('/pagamento')
def pagamento():
    id_pedido = request.args.get('id_pedido')
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT valor FROM pedidos WHERE id_pedido = %s",
        (id_pedido,)
    )
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    if resultado:
        valor = resultado[0]

        return render_template(
            'pagamento.html',
            id_pedido=id_pedido,
            valor=valor
        )
    return redirect(url_for('produtos'))

@app.route('/fazer_pagamento', methods=['POST'])
def fazer_pagamento():
    id_pedido = request.form['id_pedido']
    forma_pagamento = request.form['forma_pagamento']
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT valor FROM pedidos WHERE id_pedido = %s",
        (id_pedido,)
    )
    resultado = cursor.fetchone()
    valor = resultado[0]
    cursor.execute(
        "SELECT COALESCE(MAX(id_pagamento), 0) + 1 FROM pagamentos"
    )
    id_pagamento = cursor.fetchone()[0]
    sql = """
        INSERT INTO pagamentos (
            id_pagamento, id_pedido, forma_pagamento, valor
        )
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(
        sql,
        (id_pagamento, id_pedido, forma_pagamento, valor)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect(url_for('produtos'))

@app.route('/adicionar_carrinho', methods=['POST'])
def adicionar_carrinho():

    id_produto = request.form['id_produto']

    if 'carrinho' not in session:
        session['carrinho'] = {}

    carrinho = session['carrinho']

    if id_produto in carrinho:
        carrinho[id_produto] += 1
    else:
        carrinho[id_produto] = 1

    session['carrinho'] = carrinho

    return redirect(url_for('produtos'))


@app.route('/carrinho')
def carrinho():

    carrinho = session.get('carrinho', {})

    conexao = conectar()
    cursor = conexao.cursor()

    produtos = []
    total = 0

    for id_produto, quantidade in carrinho.items():

        cursor.execute("""
            SELECT id_produto, nome_produto, preco
            FROM produtos
            WHERE id_produto = %s
        """, (id_produto,))

        produto = cursor.fetchone()

        if produto:
            subtotal = float(produto[2]) * quantidade

            produtos.append({
                'id': produto[0],
                'nome': produto[1],
                'preco': float(produto[2]),
                'quantidade': quantidade,
                'subtotal': subtotal
            })

            total += subtotal

    cursor.close()
    conexao.close()

    return render_template(
        'carrinho.html',
        produtos=produtos,
        total=total
    )

@app.route('/remover_carrinho', methods=['POST'])
def remover_carrinho():
    id_produto = request.form['id_produto']
    carrinho = session.get('carrinho', {})
    if id_produto in carrinho:
        del carrinho[id_produto]
    session['carrinho'] = carrinho
    return redirect(url_for('carrinho'))

@app.route('/pagamentos_feitos')
def pagamentos_feitos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT
            id_pagamento,
            id_pedido,
            forma_pagamento,
            valor,
            status,
            data
        FROM pagamentos
        ORDER BY data DESC
    """)
    pagamentos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template(
        'pagamentos_feitos.html',
        pagamentos=pagamentos
    )

if __name__ == '__main__':
    app.run(debug=True)