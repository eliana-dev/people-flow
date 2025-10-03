# from flask import request
from models.empleados import Empleado, EmpleadoUpdate
from connection import collection as col
from bson.objectid import ObjectId
from datetime import datetime
from flask import jsonify

def get_all_empleados():  ## todos los empleados
    all_empleados = col.find({})
    return [document_to_json(empleado) for empleado in all_empleados]


def get_by_puesto(puesto_buscar: str):  ##filtra por puesto
    empleados = col.find({"puesto": {"$eq": puesto_buscar}})
    return [document_to_json(empleado) for empleado in empleados]


def get_by_id(id_empleado: str): ## si no hay un empleado con ese id rompe
    empleado = col.find_one({"_id": ObjectId(id_empleado)})
    if empleado is None:
        return {"error": "Empleado no encontrado."}, 404
    return document_to_json(empleado)


def create_empleado(empleado: Empleado):
    try:
        empleado.model_validate(empleado)
    except Exception as e:
        return {"error": f"Datos invalidos: {str(e)}"}, 400
    result = col.insert_one(empleado.model_dump())
    if not result.acknowledged:
        return {"error": "No se pudo agregar el empleado."}
    return {"mensaje": "Se agrego el nuevo empleado"}


def update_empleado(id_empleado: str, empleado: EmpleadoUpdate):
    filter_id = {"_id": ObjectId(id_empleado)}
    update_data = empleado.model_dump(
        exclude_none=True
    )  # convierte en dict pero excluye todos los campos que esten en none
    col.update_one(filter_id, {"$set": update_data})
    return {"mensaje": "Se actualizó el usuario"}


def delete_empleado(id_empleado: str):
    filter_id = {"_id": ObjectId(id_empleado)}
    result = col.delete_one(filter_id)
    if result.deleted_count == 0:
        return {"error": "Empleado no encontrado."}, 404
    return {"mensaje": f"Se elimino : {result.deleted_count} empleado"}


def get_promedio_salarios():
    pipeline = [{"$group": {"_id": None, "promedio_salario": {"$avg": "$salario"}}}]
    result = list(col.aggregate(pipeline))
    if result:
        return jsonify({
            "promedio_salario": result[0]["promedio_salario"]
            })
    return jsonify({"promedio_salario": None})


### utils

def document_to_json(document):
    document["_id"] = str(document["_id"])
    document["fecha_ingreso"] = datetime.strftime(document["fecha_ingreso"], "%Y-%m-%d")
    return document
