from pymongo import MongoClient
from config import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_USER,
    MONGO_PASS,
    MONGO_AUTH_MECHANISM,
)

client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USER,
    password=MONGO_PASS,
    authMechanism=MONGO_AUTH_MECHANISM,
)

db = client.peopleFlow
collection = db.empleados
