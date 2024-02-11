from flask import Flask, render_template, request, redirect, send_file
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
    new_user = User(
        name=name,
        surname=surname,
        email=email,
        username=username,
        password=password
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")


@app.route("/registration")
def registration():
    return render_template("registr.html")

@app.route("/shop", methods=["GET", "POST"])
def recombination():
    cost = None
    foos = {
        "pancake": 20,
        "slapjack":30,
        "gingerbread":10,
    }
    values_list = list(foos.values())
    keys_list = list(foos.keys())
    sums = []
    if request.method == "POST":


        for i in range(len(keys_list)):
            try:
                pancake = int(request.form.get(f"{keys_list[0]}", ""))
            except:
                return '<a href="http://127.0.0.1:5000/shop">cсылка на магазин</a>'
            res = values_list[i] * pancake
            sums.append(res)
        cost = sum(sums)

    return render_template("shop.html", cost=cost)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
