# from flask import request
from models.empleados import Empleado, EmpleadoUpdate
from connection import collection as col
from bson.objectid import ObjectId
from datetime import datetime
from flask import jsonify
from logger import logger

def get_all_empleados():  ## todos los empleados
    logger.info("Iniciando búsqueda de todos los empleados")
    all_empleados = col.find({})
    empleados_list = [document_to_json(empleado) for empleado in all_empleados]
    logger.info(f"Se encontraron {len(empleados_list)} empleados")
    return empleados_list


def get_by_puesto(puesto_buscar: str):  ##filtra por puesto
    logger.debug(f"Buscando empleados con puesto: {puesto_buscar}")
    empleados = col.find({"puesto": {"$eq": puesto_buscar}})
    empleados_list = [document_to_json(empleado) for empleado in empleados]
    logger.info(f"Se encontraron {len(empleados_list)} empleados con puesto '{puesto_buscar}'")
    return empleados_list


def get_by_id(id_empleado: str): 
    logger.debug(f"Buscando empleado con ID: {id_empleado}")
    try:
        empleado = col.find_one({"_id": ObjectId(id_empleado)})
        if empleado is None:
            logger.warning(f"Empleado no encontrado con ID: {id_empleado}")
            return {"error": "Empleado no encontrado."}, 404
        logger.info(f"Empleado encontrado con ID: {id_empleado}")
        return document_to_json(empleado)
    except Exception as e:
        logger.error(f"Error al buscar empleado con ID {id_empleado}: {str(e)}")
        return {"error": "ID de empleado inválido."}, 400


def create_empleado(empleado: Empleado):
    logger.debug(f"Intentando crear nuevo empleado: {empleado.nombre}")
    try:
        empleado.model_validate(empleado)
        logger.debug("Validación de datos exitosa")
    except Exception as e:
        logger.error(f"Error de validación al crear empleado: {str(e)}")
        return {"error": f"Datos invalidos: {str(e)}"}, 400
    
    result = col.insert_one(empleado.model_dump())
    if not result.acknowledged:
        logger.error("Error: No se pudo agregar el empleado a la base de datos")
        return {"error": "No se pudo agregar el empleado."}
    
    logger.info(f"Empleado creado exitosamente con ID: {result.inserted_id}")
    return {"mensaje": "Se agrego el nuevo empleado"}


def update_empleado(id_empleado: str, empleado: EmpleadoUpdate):
    logger.debug(f"Actualizando empleado con ID: {id_empleado}")
    try:
        filter_id = {"_id": ObjectId(id_empleado)}
        update_data = empleado.model_dump(
            exclude_none=True
        )  # convierte en dict pero excluye todos los campos que esten en none
        logger.debug(f"Datos a actualizar: {update_data}")
        
        result = col.update_one(filter_id, {"$set": update_data})
        if result.matched_count == 0:
            logger.warning(f"No se encontró empleado con ID: {id_empleado}")
            return {"error": "Empleado no encontrado."}, 404
        
        logger.info(f"Empleado actualizado exitosamente con ID: {id_empleado}")
        return {"mensaje": "Se actualizó el usuario"}
    except Exception as e:
        logger.error(f"Error al actualizar empleado con ID {id_empleado}: {str(e)}")
        return {"error": "Error al actualizar el empleado."}, 500


def delete_empleado(id_empleado: str):
    logger.debug(f"Eliminando empleado con ID: {id_empleado}")
    try:
        filter_id = {"_id": ObjectId(id_empleado)}
        result = col.delete_one(filter_id)
        if result.deleted_count == 0:
            logger.warning(f"No se encontró empleado para eliminar con ID: {id_empleado}")
            return {"error": "Empleado no encontrado."}, 404
        
        logger.info(f"Empleado eliminado exitosamente con ID: {id_empleado}")
        return {"mensaje": f"Se elimino : {result.deleted_count} empleado"}
    except Exception as e:
        logger.error(f"Error al eliminar empleado con ID {id_empleado}: {str(e)}")
        return {"error": "Error al eliminar el empleado."}, 500


def get_promedio_salarios():
    logger.info("Calculando promedio de salarios")
    try:
        pipeline = [{"$group": {"_id": None, "promedio_salario": {"$avg": "$salario"}}}]
        result = list(col.aggregate(pipeline))
        if result:
            promedio = result[0]["promedio_salario"]
            logger.info(f"Promedio de salarios calculado: {promedio}")
            return jsonify({
                "promedio_salario": promedio
                })
        logger.warning("No se encontraron empleados para calcular promedio")
        return jsonify({"promedio_salario": None})
    except Exception as e:
        logger.error(f"Error al calcular promedio de salarios: {str(e)}")
        return jsonify({"error": "Error al calcular promedio de salarios"}), 500


### utils

def document_to_json(document):
    document["_id"] = str(document["_id"])
    document["fecha_ingreso"] = datetime.strftime(document["fecha_ingreso"], "%Y-%m-%d")
    return document
