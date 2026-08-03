#request lê informações que são enviadas pelo navegador
#make_response permite criar respostas personalizadas
from flask import render_template, request, make_response, redirect, abort

#a função recebe o app e adocopma as rotas
def registrar_rotas(app):

    @app.route("/")
    def hello():
        return render_template("index.html")

    @app.route("/nome")
    def nome():
        return render_template("nome.html")

    @app.route("/codigostatusdiferente")
    def bad_request():

        #Que diz que algo foi feito de forma errada
        #O número 400 seginifica Bad Request
        return "Bad request", 400

    @app.route("/objetoresposta")
    def cookie():

        #Cria uma reposta
        resposta = make_response("<h1>This document carries a cookie!</h1>")

        #Nome do cookie: disciplina
        #Valor: PTBDSWS
        resposta.set_cookie("disciplina", "PTBDSWS")

        #envia reposta ao navegador
        return resposta

    @app.route("/contextorequisicao")
    def navegador():
        return request.headers.get("User-Agent")

    @app.route("/ifsp")
    def ifsp():

        #direciona para o endereço
        return redirect("https://ptb.ifsp.edu.br/")

    @app.route("/notfound")
    def not_found():
        #abort (404) interrompe aexecução e devolve o erro
        #Siginifica que não é possível encontrar a página
        abort(404)