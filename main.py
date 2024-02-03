from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/registration")
def registration():
    return render_template("registr.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")


if __name__ == "__main__":
    app.run(debug=True)