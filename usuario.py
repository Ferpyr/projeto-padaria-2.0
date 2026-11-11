from conexao import conectar

def validar_login(email, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE email = %s AND senha = %s",
        (email, senha)
    )

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        return True
    else:
        return False