from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)


def conectar_banco():

    conexao = sqlite3.connect("biblioteca.db")

    return conexao



def buscar_livros():

    banco = conectar_banco()

    cursor = banco.cursor()

    cursor.execute("SELECT * FROM livros")

    livros = cursor.fetchall()

    banco.close()

    return livros



@app.route("/", methods=["GET", "POST"])
def inicio():

    titulo = ""
    autor = ""

    if request.method == "POST":

        titulo = request.form["titulo"]
        autor = request.form["autor"]

        banco = conectar_banco()

        cursor = banco.cursor()

        cursor.execute(
            "INSERT INTO livros (titulo, autor) VALUES (?, ?)",
            (titulo, autor)
        )

        banco.commit()

        banco.close()


    livros = buscar_livros()


    return render_template(
        "index.html",
        titulo=titulo,
        autor=autor,
        livros=livros
    )



@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):

    banco = conectar_banco()

    cursor = banco.cursor()


    cursor.execute(
        "DELETE FROM livros WHERE id = ?",
        (id,)
    )


    banco.commit()

    banco.close()


    return redirect("/")



if __name__ == "__main__":

    app.run(debug=True)