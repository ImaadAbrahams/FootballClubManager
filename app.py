from flask import Flask, redirect, render_template, request

app = Flask(__name__)

players = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    if request.method == "POST":
        player = {
            "name": request.form["name"],
            "age": request.form["age"],
            "position": request.form["position"]
        }
        players.append(player)
        return redirect("/players")
    
    return render_template("add_player.html")

@app.route("/players")
def view_players():
    return render_template("players.html", players=players)

if __name__ == "__main__":
    app.run(debug=True)