from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:imaaddb03@localhost/football_club_manager"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
players = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    if request.method == "POST":
        new_player = Player(
            name = request.form["name"],
            age = request.form["age"],
            position = request.form["position"]
        )
        
        db.session.add(new_player)
        db.session.commit()
        return redirect("/players")
    
    return render_template("add_player.html")

@app.route("/players")
def view_players():
    players = Player.query.all()
    return render_template("players.html", players=players)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String (50), nullable=False)

if __name__ == "__main__":
    app.run(debug=True)