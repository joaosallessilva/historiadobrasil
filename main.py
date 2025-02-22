from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/figuras_historicas")
def figuras_historicas():
    return render_template("figuras_historicas.html")


@app.route("/periodos_historicos")
def periodos_historicos():
    return render_template("periodos_historicos.html")



@app.route("/curiosidades")
def curiosidades():
    return render_template("curiosidades.html")


app.run(debug=True)
