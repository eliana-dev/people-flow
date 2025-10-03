from datetime import datetime
from pydantic import BaseModel, Field


class Empleado(BaseModel):
    nombre: str  # Si no se le pone un valor por defecto entonces considera que es obligatirio
    apellido: str
    email: str
    puesto: str
    salario: float
    fecha_ingreso: datetime = Field(default_factory=datetime.now)


class EmpleadoUpdate(BaseModel): # modelo usado para actualizar, si no se pasa los valores toma none por defecto
    nombre: str = None
    apellido: str = None
    email: str = None
    puesto: str = None
    salario: float = None
    fecha_ingreso: datetime = None
