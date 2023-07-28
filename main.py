# Autor: Nilton F L
# Data: 28 de Julho de 2023
# Versão: 1.0

# bibliotecas a instalar:
# pip install flask flask-socketio python-socketio simple-websocket

# Importações necessárias
# Esta linha importa as classes Flask (que é a base do aplicativo web) e render_template (usada para renderizar páginas HTML).
from flask import Flask, render_template, url_for

# Aqui, importamos as classes SocketIO (para gerenciar a comunicação em tempo real, como o chat)
# e send (para enviar mensagens através do SocketIO).
from flask_socketio import SocketIO, send

# Criação do aplicativo Flask
# Essa linha cria uma instância da classe Flask e associa-a à variável app. Isso é feito para criar o aplicativo web.
app = Flask(__name__)

#  Aqui, definimos uma chave de segurança (SECRET) para o aplicativo. Essa chave é usada para fins de segurança, como assinar cookies e tokens.
app.config["SECRET"] = "DKINBTES3HC2GY5CBFJDCQ2SYHV6A6XXVTJFSA"

# Essa configuração define o modo de depuração do aplicativo como verdadeiro (True), o que permite que você visualize detalhes de erros e outras informações úteis durante o desenvolvimento.
# No ambiente de produção, você normalmente definiria isso como falso (False).
app.config["DEBUG"] = False

# Criamos uma instância do SocketIO, associada à variável socketio, e passamos o aplicativo app como parâmetro.
# O parâmetro cors_allowed_origins="*" indica que o SocketIO permitirá conexões de qualquer origem,
# o que pode ser útil durante o desenvolvimento, mas pode ser ajustado para melhorar a segurança em produção.
socketio = SocketIO(app, cors_allowed_origins="*")

# Esta é uma decoradora (@) que indica que a função logo abaixo será acionada quando o evento "message" ocorrer no SocketIO.


@socketio.on("message")
# Essa função, gerenciar_mensagens, será chamada sempre que uma mensagem for enviada através do evento "message".
# A mensagem é passada como parâmetro para a função.
def gerenciar_mensagens(mensagem):
    # Aqui, a função imprime a mensagem recebida no console.
    print(f"Mensagem: {mensagem}")
    # Essa linha envia a mensagem recebida para todos os clientes conectados ao site, graças ao parâmetro broadcast=True.
    send(mensagem, broadcast=True)

# Essa é outra decoradora (@) que indica que a função seguinte será chamada quando a rota padrão ("/") do site for acessada.


@app.route("/")
# Esta é a função que será chamada quando a rota padrão ("/") for acessada.
def home():
    # Aqui, a função home() renderiza o arquivo "index.html" usando a função render_template do Flask.
    # Isso significa que quando alguém acessar o site principal, a página "index.html" será exibida.
    return render_template("index.html")


# Esta linha verifica se o arquivo está sendo executado diretamente como um programa (em oposição a ser importado como um módulo).
if __name__ == "__main__":
    # Se o arquivo estiver sendo executado diretamente, o aplicativo Flask será executado no servidor local (localhost) junto com o SocketIO,
    # permitindo a comunicação em tempo real.
    # Isso significa que o site estará disponível na internet em que o seu computador está conectado, tornando-o acessível para outros dispositivos na mesma rede local.
    # Note que, em um ambiente de produção, você normalmente usaria um servidor web como o Gunicorn ou uWSGI para servir o aplicativo Flask.
    socketio.run(app, host='localhost')
