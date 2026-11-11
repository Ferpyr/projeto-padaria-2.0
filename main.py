from flask import Flask, render_template, request
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

@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')
if __name__ == '__main__':
    app.run(debug=True)