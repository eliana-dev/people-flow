from flask import Blueprint, jsonify, request
from controllers import empleados_crud
from models.empleados import Empleado, EmpleadoUpdate
from pydantic import ValidationError
from bson import ObjectId

bp = Blueprint("empleados", __name__, url_prefix="/empleados")


@bp.route("/", methods=["GET"])
def get_empleados():
    """
    Endpoint para obtener todos los empleados registrados.
    ---
    tags:
        - Empleados
    responses:
        200:
            description: Retorna un objeto con los datos del empleado.
            schema:
                type: object
                properties:
                    nombre:
                        type: string
                        example: Eliana
                    apellido:
                        type: string
                        example: Valdez
                    email:
                        type: string
                        example: valdezeliana@gmail.com
                    puesto:
                        type: string
                        example: Backend Developer JR
                    salario:
                        type: number
                        format: float
                        example: 1250
                    fecha_ingreso:
                        type: string
                        format: date-time

    """
    return jsonify(empleados_crud.get_all_empleados())


@bp.route("/puesto/<string:puesto>", methods=["GET"])
def get_empleado_by_puesto(puesto: str):
    """
    Endpoint para obtener todos los empleados de un puesto especifico.
    ---
    tags:
        - Empleados
    parameters:
        -   name: puesto
            in: path
            type: string
            required: true
            description: Puesto del empleado.
    responses:
        200:
            description: Retorna un objeto con los datos del empleado.
            schema:
                type: object
                properties:
                    nombre:
                        type: string
                        example: Eliana
                    apellido:
                        type: string
                        example: Valdez
                    email:
                        type: string
                        example: valdezeliana38@gmail.com
                    puesto:
                        type: string
                        example: Backend Developer JR
                    salario:
                        type: number
                        format: float
                        example: 1250
                    fecha_ingreso:
                        type: string
                        format: date-time

    """
    return jsonify(empleados_crud.get_by_puesto(puesto))


@bp.route("/<string:id>", methods=["GET"])
def get_empleado_by_id(id: str):
    """
    Endpoint para obtener un empleado por su id.
    ---
    tags:
        - Empleados
    parameters:
        -   name: id
            in: path
            type: string
            required: true
            description: id del empleado.
    responses:
        200:
            description: Retorna un objeto con los datos del empleado.
            schema:
                type: object
                properties:
                    nombre:
                        type: string
                        example: Eliana
                    apellido:
                        type: string
                        example: Valdez
                    email:
                        type: string
                        example: valdezeliana38@gmail.com
                    puesto:
                        type: string
                        example: Backend Developer JR
                    salario:
                        type: number
                        format: float
                        example: 1250
                    fecha_ingreso:
                        type: string
                        format: date-time

    """
    if not ObjectId.is_valid(id):
        return jsonify({"error": "El ID es inválido"}), 400
    return jsonify(empleados_crud.get_by_id(id))


@bp.route("/", methods=["POST"])
def create_empleado():
    """
    Endpoint registrar nuevos empleados.
    ---
    tags:
        - Empleados
    parameters:
    -   in: body
        name: body
        required: true
        schema:
            type: object
            properties:
                nombre:
                    type: string
                    example: Maria
                apellido:
                    type: string
                    example: Rodriguez
                email:
                    type: string
                    example: rodriguezMaria@gmail.com
                puesto:
                    type: string
                    example: Frontend developer JR
                salario:
                    type: number
                    format: float
                    example: 1500
    responses:
        200:
            description: Registra un nuevo empleado.
            schema:
                type: object
                properties:
                    nombre:
                        type: string
                        example: Eliana
                    apellido:
                        type: string
                        example: Valdez
                    email:
                        type: string
                        example: valdezeliana38@gmail.com
                    puesto:
                        type: string
                        example: Backend Developer JR
                    salario:
                        type: number
                        format: float
                        example: 1250
                    fecha_ingreso:
                        type: string
                        format: date-time
    """
    data = request.get_json()
    try:
        empleado = Empleado.model_validate(data)
    except ValidationError as e:
        return {"error": f"Datos que faltan: {e.errors()[0]['loc'][0]}"}, 400
    return empleados_crud.create_empleado(empleado)


@bp.route("/<string:id>", methods=["PATCH"])
def patch_empleado(id: str):
    """
    Endpoint para actualizar empleados.
    ---
    tags:
        - Empleados
    parameters:
    -   name: id
        in: path
        type: string
        required: true
        description: id del Empleado.
    -   in: body
        name: body
        required: true
        schema:
            type: object
            properties:
                nombre:
                    type: string
                    example: Maria
                apellido:
                    type: string
                    example: Rodriguez
                email:
                    type: string
                    example: rodriguezMaria@gmail.com
                puesto:
                    type: string
                    example: Frontend developer JR
                salario:
                    type: number
                    format: float
                    example: 1500
                fecha_ingreso:
                    type: string
                    format: date-time
    responses:
        200:
            description: Actualiza los datos del empleado.
            schema:
                type: object
                properties:
                    nombre:
                        type: string
                        example: Eliana
                    apellido:
                        type: string
                        example: Valdez
                    email:
                        type: string
                        example: valdezeliana38@gmail.com
                    puesto:
                        type: string
                        example: Backend Developer JR
                    salario:
                        type: number
                        format: float
                        example: 1250
                    fecha_ingreso:
                        type: string
                        format: date-time
    """
    if not ObjectId.is_valid(id):
        return jsonify({"error": "El ID es inválido"}), 400

    data = request.get_json()  # obtenemos el json del body
    empleado = EmpleadoUpdate.model_validate(
        data
    )  # valida que la data tenga el mismo formato que el modelo
    return empleados_crud.update_empleado(id_empleado=id, empleado=empleado)


@bp.route("/<string:id>", methods=["DELETE"])
def delete_empleado(id: str):
    """
    Endpoint para eliminar un empleado por su id.
    ---
    tags:
        - Empleados
    parameters:
        -   name: id
            in: path
            type: string
            required: true
            description:  ID del empleado a eliminar.
    responses:
        200:
            description: Empleado eliminado del registro.
            schema:
                type: object
                properties:
                    mensaje:
                        type: string
                        example: "Empleado eliminado con éxito"
        404:
            description: No sé encontro el empleado.
            schema:
                type:
                properties:
                    error:
                        type: string
                        example: "Empleado no encontrado"

    """
    if not ObjectId.is_valid(id):
        return jsonify({"error": "El ID es inválido"}), 400
    return empleados_crud.delete_empleado(id)


@bp.route("/promedio-salarial", methods=["GET"])
def get_promedio_salarial():
    """
    Endpoint para obtener el promedio salarial de todos los empleados.
    ---
    tags:
        - Empleados
    responses:
        200:
            description: Retorna un objeto con el promedio salarial.
            schema:
                type: object
                properties:
                    promedio_salario:
                        type: number
                        format: float
                        example: 1500
    """
    return empleados_crud.get_promedio_salarios()
