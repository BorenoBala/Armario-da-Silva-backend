app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sua_senha'
app.config['MYSQL_DB'] = 'meu_banco_de_dados'

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações do servidor de e-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'seu_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'sua_senha'
app.config['MAIL_DEFAULT_SENDER'] = 'seu_email@gmail.com'

mail = Mail(app)

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

@app.route('/tela_entar')
def inicio():
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

        cursor = mysql.connection.cursor()

        cursor.execute("UPDATE usuarios SET senta=%s WHERE email=%s", (senha_hash, email))
        mysql.connection.commit()

        cursor.close()
        return "senha atualizada!"

    return redirect (url_for('login'))

    from itsdangerous import URLSafeTimeSerializer

def criar_token(email):
    s = URLSafeTimeSerializer(app.config[''])
    return s.dumps(email, salt='recuperação de senha')

def verificar_token(token, expiration=10000):
    s = URLSafeTimeSerializer(app.config[''])
    try:
        email = s.load(token, salt='recuperação de senha', max_age=expiration)
    except: 
        return False
        printf({email})

@app.route('/recuperacao', methods=['get', 'post'])
def recuperacao():
    if request.method == 'post':
        email = request.form['email']

    cursor =  mysql.connection.cursor()
    cursor.execute ("select * From usuarios whare email=%s", (email))
    usuario = cursor.fetchone()
    
    if not usuario:
        return "Usuário não encontrado", 404

        token = criar_token(email)

        link_recuperacao = url_for('resetar_senha', token=token, external=True)

        msg = Message('Recuperação de senha',
                        recipments=[email])
        msg.body = f'Para redefinir a senha da sua conta, clieque aqui{link_recupercao}'
        mail.send(msg)

        return "Um e-mail de recuperação foi enviado!", 200

    return render_template(esqueci_senha)