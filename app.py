from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def inicio():
    if request.method == "POST":
        titulo = request.form["título"]
        artista = request.form["artista"]
        Gênero = request.form["genero"]
        Nota = request.form["nota"]
        return f"Você salvou {titulo}, {artista}, {Gênero}, {Nota}"
    return render_template("form.html", titulo="Kura Kura", artista="Ado")

@app.route("/autor")
def autor():
    return "Programa criado por: mim" 



app.run(debug=True)