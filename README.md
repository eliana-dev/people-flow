# PeopleFlow 📊

Una API REST para gestión de empleados desarrollada con Flask y MongoDB. Permite realizar operaciones CRUD completas sobre registros de empleados, incluyendo consultas especializadas como el promedio salarial.

## Características

- ✅ **CRUD completo de empleados** (Crear, Leer, Actualizar, Eliminar)
- 🔍 **Búsquedas especializadas** por ID y puesto de trabajo
- 📊 **Cálculo de promedio salarial**
- ✅ **Validación de datos** con Pydantic
- 🗄️ **Base de datos MongoDB**
- 🚀 **API REST con Flask**

## Tecnologías

- **Python 3.9+**
- **Flask** - Framework web
- **PyMongo** - Driver de MongoDB
- **Pydantic** - Validación de datos
- **python-dotenv** - Gestión de variables de entorno
- **Flasgger** - Documentación de API con Swagger
- **colorlog** – Logs coloreados y más legibles
  
## Requisitos previos

### Opción 1: Usando uv (Recomendado)

- [uv](https://docs.astral.sh/uv/) - Gestor de paquetes rápido de Python
- MongoDB instalado y ejecutándose

### Opción 2: Usando Python tradicional

- Python 3.9 o superior
- pip (incluido con Python)
- MongoDB instalado y ejecutándose

## Instalación y configuración

### 🔧 Configuración de variables de entorno

1. **Copia el archivo de ejemplo de configuración:**

   ```bash
   cp .env.example .env
   ```

2. **Edita el archivo `.env`** con tus datos de MongoDB:

   ```env
   MONGO_HOST=localhost
   MONGO_PORT=27017
   MONGO_USER=tu_usuario_de_mongodb
   MONGO_PASS=tu_contraseña_de_mongodb
   MONGO_AUTH_MECHANISM=SCRAM-SHA-256
   ```

   > **Nota:** Si tu MongoDB no tiene autenticación habilitada, puedes dejar `MONGO_USER` y `MONGO_PASS` vacíos.

### 🚀 Opción 1: Instalación con uv (Recomendado)

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd people-flow

# Instalar dependencias con uv
uv sync

# Ejecutar la aplicación
uv run python src/main.py
```

### 🐍 Opción 2: Instalación con Python tradicional

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd people-flow

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python src/main.py
```

## 🌐 Uso de la API

La API estará disponible en `http://localhost:5000`

### Endpoints disponibles

#### 🔍 Estado de la API

```http
GET /alive
```

Respuesta: `"PeopleFlow▶ API is Alive!"`

#### 👥 Gestión de empleados

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/empleados/` | Obtener todos los empleados |
| `GET` | `/empleados/{id}` | Obtener empleado por ID |
| `GET` | `/empleados/puesto/{puesto}` | Obtener empleados por puesto |
| `POST` | `/empleados/` | Crear nuevo empleado |
| `PATCH` | `/empleados/{id}` | Actualizar empleado |
| `DELETE` | `/empleados/{id}` | Eliminar empleado |
| `GET` | `/empleados/promedio-salarial` | Obtener promedio salarial |

## 📊 Modelo de datos

### Empleado

```json
{
  "nombre": "string (requerido)",
  "apellido": "string (requerido)",
  "email": "string (requerido)",
  "puesto": "string (requerido)",
  "salario": "number (requerido)",
  "fecha_ingreso": "datetime (automático si no se especifica)"
}
```

## 🛠️ Desarrollo

### Estructura del proyecto

```
people-flow/
├── src/
│   ├── main.py              # Punto de entrada de la aplicación
│   ├── config.py            # Configuración y variables de entorno
│   ├── connection.py        # Conexión a MongoDB
│   ├── blueprints/
│   │   └── empleados.py     # Rutas de la API
│   ├── controllers/
│   │   └── empleados_crud.py # Lógica de negocio
│   └── models/
│       └── empleados.py     # Modelos de datos con Pydantic
├── .env.example             # Ejemplo de configuración
├── .env                     # Configuración local (no subir a git)
├── requirements.txt         # Dependencias para pip
├── pyproject.toml          # Configuración del proyecto para uv
└── README.md               # Este archivo
```

### Variables de entorno requeridas

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `MONGO_HOST` | Host de MongoDB | `localhost` |
| `MONGO_PORT` | Puerto de MongoDB | `27017` |
| `MONGO_USER` | Usuario de MongoDB | `admin` |
| `MONGO_PASS` | Contraseña de MongoDB | `password123` |
| `MONGO_AUTH_MECHANISM` | Mecanismo de autenticación | `SCRAM-SHA-256` |
