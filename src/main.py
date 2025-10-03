from flask import Flask
from flasgger import Swagger
from blueprints import empleados

app = Flask(__name__)

template = {
    "swagger": "2.0",
    "info": {
        "title": "PeopleFlow▶",
        "description": "Documentación de la API de PeopleFlow▶",
        "version": "1.0.0",
    },
}
swagger = Swagger(app, template=template)
app.register_blueprint(blueprint=empleados.bp)


@app.route("/alive")
def alive_msg():
    """
    Endpoint para comprobar el estado de la API
    ---
    tags:
        - Health Check
    responses:
        200:
            description: Retorna un mensaje con el estado de la API
            schema:
                type: string
                example: "PeopleFlow▶ API is Alive!"
    """
    return "PeopleFlow▶ API is Alive!"


if __name__ == "__main__":
    app.run(debug=True)
