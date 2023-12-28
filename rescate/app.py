from flask import Flask, render_template


# inicializacion
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/productos")
def productos():
    return render_template("productos.html")


@app.route("/cesta")
def cesta():
    return render_template("cesta.html")


@app.route("/registro")
def pregistro():
    return render_template("registro.html")


@app.route("/acceder")
def acceder():
    return render_template("acceder.html")


# correr la aplicacion
if __name__ == "__main__":
    app.run(debug=True)
