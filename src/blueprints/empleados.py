from flask import Blueprint, jsonify, request
from controllers import empleados_crud
from models.empleados import Empleado, EmpleadoUpdate
from pydantic import ValidationError
from bson import ObjectId

bp = Blueprint("empleados", __name__, url_prefix="/empleados")


@bp.route("/", methods=["GET"])
def get_empleados():
    return jsonify(empleados_crud.get_all_empleados())


@bp.route("/puesto/<string:puesto>", methods=["GET"])
def get_empleado_by_puesto(puesto: str):
    return jsonify(empleados_crud.get_by_puesto(puesto))


@bp.route("/<string:id>", methods=["GET"])
def get_empleado_by_id(id: str):
    if not ObjectId.is_valid(id):
        return jsonify({"error": "El ID es inválido"}), 400
    return jsonify(empleados_crud.get_by_id(id))


@bp.route("/", methods=["POST"])
def create_empleado():
    data = request.get_json()
    try:
        empleado = Empleado.model_validate(data)
    except ValidationError as e:
        return {"error": f"Datos que faltan: {e.errors()[0]['loc'][0]}"}, 400
    return empleados_crud.create_empleado(empleado)


@bp.route("/<string:id>", methods=["PATCH"])
def patch_empleado(id: str):
    if not ObjectId.is_valid(id):
        return jsonify({"error": "El ID es inválido"}), 400

    data = request.get_json()  # obtenemos el json del body
    empleado = EmpleadoUpdate.model_validate(
        data
    )  # valida que la data tenga el mismo formato que el modelo
    return empleados_crud.update_empleado(id_empleado=id, empleado=empleado)


@bp.route("/<string:id>", methods=["DELETE"])
def delete_empleado(id: str):
    if not ObjectId.is_valid(id):
        return jsonify({"error": "El ID es inválido"}), 400
    return empleados_crud.delete_empleado(id)

@bp.route("/promedio-salarial", methods=["GET"])
def get_promedio_salarial():
    return empleados_crud.get_promedio_salarios()