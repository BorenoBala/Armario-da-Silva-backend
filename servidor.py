app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sua_senha'
app.config['MYSQL_DB'] = 'meu_banco_de_dados'

@app.route('/tela_cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        cpf = request.form['cpf']
        endereco = request.form ['endereco']
        data_nascimento = request.form ['data_nascimento']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO usuario (nome, email, senha, cpf, endereco, data_nascimento) VALUES (%s, %s, %s)", (nome, email, senha, cpf, endereco, data_nascimento))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('list_users'))
    return render_template('tela_inicio.html')

   
@app.route('/tela_entrar', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nome = %s AND senha = %s", (email, senha))
        user = cursor.fetchone()
        cursor.close()
        if user:
            return redirect(url_for('tela_inicio'))
        else:
            return "Usuário ou senha inválidos!"
    return render_template('tela_entrar.html')

@app.route('/')
def home():
    return render_template('tela_inicio.html')

@app.route('/esqueci_senha', methos=['get', 'post'])
def esqueci_senha():
    if request.method == 'post':
        email = request.form[email]
        nova_senha = request.form[nova_senha]
        confirmacao_senha = request.form[confirmacao_senha]

        if confirmacao_senha!= nova_senha:
            return "As senhas não são iguais. Tente novamente"

        from werkzeug.security import generate_password_hash
        senha_hash = generate_password_hash(nova_senha)

        cursor = mysql.connection.cursor ()

        cursor.execute("UPDATE usuarios SET senta=%s WHERE email=%s", (senha_hash, email))
        mysql.connection.commit ()

        cursor.close()
        return "senha atualizada!"

    return redirect (url_for('login'))