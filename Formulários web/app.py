from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

#configuração do aplicativo
app.config['SECRET_KEY'] = 'minha-chave-secreta'

#inicia o bootstrap
bootstrap = Bootstrap(app)

#Registra Rotas
from routes import registrar_rotas
registrar_rotas(app)

if __name__ == '__main__':
    app.run(debug=True)