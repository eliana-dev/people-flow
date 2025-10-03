from flask import Flask
from blueprints import empleados

app = Flask(__name__)
app.register_blueprint(blueprint=empleados.bp)


@app.route("/alive")
def alive_msg():
    return "PeopleFlow▶ API is Alive!"


if __name__ == "__main__":
    app.run(debug=True)
