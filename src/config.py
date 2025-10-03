from dotenv import load_dotenv
import os

load_dotenv()

MONGO_HOST = (os.getenv("MONGO_HOST"),)
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_AUTH_MECHANISM = os.getenv("MONGO_AUTH_MECHANISM", "SCRAM-SHA-256")
