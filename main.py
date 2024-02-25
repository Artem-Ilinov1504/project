from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    num_card = db.Column(db.Integer, nullable=False)
    srok = db.Column(db.Integer, nullable=False)
    CVV = db.Column(db.Integer, nullable=False)

@app.route("/")
def index():
    users = User.query.all()
    print(users)
    return render_template("index.html", users=users)

@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form["name"]
    surname = request.form["surname"]
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    num_card = request.form["num_card"]
    srok = request.form["srok"]
    CVV = request.form["CVV"]
    new_user = User(
        name=name,
        surname=surname,
        email=email,
        username=username,
        password=password,
        num_card=num_card,
        srok=srok,
        CVV=CVV,
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")



@app.route("/registration")
def registration():

    return render_template("registr.html")


@app.route("/shop", methods=["GET", "POST"])
def shop():

    cost = None
    foos = {
        "pancake": 20,
        "slapjack":30,
        "gingerbread":10,
        "zapecanka":75,
        "pancake2":40,
        "verguns":30,
    }
    values_list = list(foos.values())
    keys_list = list(foos.keys())
    sums = []
    if request.method == "POST":


        for i in range(len(keys_list)):
            try:
                pancake = int(request.form.get(f"{keys_list[0]}", ""))
            except:
                return '<a href="http://127.0.0.1:5000/shop">Посилання на магазин</a>'
            res = values_list[i] * pancake
            sums.append(res)
        cost = sum(sums)

    return render_template("shop.html", cost=cost)

@app.route("/goodbye")
def goodbye():
    return '<p>Оплачено. Дякую</p>'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
