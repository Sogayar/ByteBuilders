from flask import Flask, jsonify, render_template, request, abort, redirect, url_for

app = Flask(__name__, template_folder = 'C:/Users/henri/Desktop/Estudos/HTML/ByteBuilders/templates',static_folder = 'static', static_url_path = '/static')
app.config['SECRET_KEY'] = 'Senha'

@app.route('/')
def teste():
    return render_template ('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    nome = request.form.get('nome') # o que esta entre 'aspas' deve ser o "name" do input no HTML
    senha = request.form.get('senha') # o que esta entre 'aspas' deve ser o "senha" do input no HTML
    return redirect('/')



@app.route("/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("perfil.html", nome_usuario = nome_usuario)

# def valid_login(username, password):
#     # Lógica para validar o login
#     # Exemplo básico, substitua pela sua lógica de validação
#     return username == "admin" and password == "secret"

# def log_the_user_in(username):
#     # Lógica para logar o usuário
#     return f"Usuário {username} logado com sucesso!"

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'], request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     return render_template('login.html', error = error)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
