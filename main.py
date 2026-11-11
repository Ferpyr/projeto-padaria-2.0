from flask import Flask, render_template, request, redirect, url_for

from conexao import conectar
from usuario import validar_login

app=Flask(__name__)
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

if __name__ == '__main__':
    app.run(debug=True)