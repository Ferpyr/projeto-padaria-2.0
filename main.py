from flask import Flask, render_template

app=Flask()

@app.route('/', methods=['GET'])
def pao():
    return render_template('pag-pao.html')

@app.route('/')
def about():
    return render_template('.html')