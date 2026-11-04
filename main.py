from flask import Flask, render_template

app=Flask()

@app.route('/', methods=['GET'])
def pao():
    return render_template('Nome do negocio.html')

@app.route('/')
def about():
    return render_template('Nome do negocio.html')