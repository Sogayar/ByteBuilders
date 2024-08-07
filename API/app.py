from flask import Flask, jsonify, render_template, request, abort, redirect, url_for

# from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)

# @app.route('/')
# def homepage():
#     return render_template("index.html")

@app.route('/')
def teste():
    return "teste"

@app.route("/<nome_usuario>")                                          # Cria uma pagina personalizada
def usuarios(nome_usuario):
    return render_template("perfil.html", nome_usuario = nome_usuario)

# @app.route('/register', methods=['POST'])
# def register():
#     # Função usando flask que registre no BD

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], # type: ignore
                       request.form['password']):
            return log_the_user_in(request.form['username']) # type: ignore
        else:
            error = 'Invalid username/password'
    # O código abaixo é executado se o método de solicitação for GET ou as credenciais forem inválidas
    return render_template('login.html', error = error) # Necessária criação de página de login

#if __name__ == "__main__":
app.run(debug = True)