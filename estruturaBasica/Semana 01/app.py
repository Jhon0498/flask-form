#Onde será construído o site.
from flask import Flask
from routes import registrar_rotas

#Cria o app
app = Flask(__name__)

#Registra todas as rotas que estão no arquivo routes.py
registrar_rotas(app)

if __name__ == "__main__":

    # Inicia o servidor
    # debug=True quer dizer:
    # "Se acontecer algum erro, me mostre exatamente onde foi."
    app.run(debug=True)