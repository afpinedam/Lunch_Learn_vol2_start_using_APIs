# Lunch & Learn: empezar a usar APIs

Este repositorio acompaña una presentación introductoria sobre cómo empezar a utilizar APIs desde cero. Su propósito es explicar cómo se comunican dos sistemas y mostrar, con ejemplos en Python, cómo consumir una API y cómo crear una API sencilla.

## ¿Qué es una API?

Una API (*Application Programming Interface*) es un contrato de comunicación que permite que dos sistemas intercambien información o ejecuten acciones de forma controlada. El flujo básico es:

1. Un cliente envía una petición (*request*) a un endpoint.
2. El servicio procesa la petición.
3. El servicio devuelve una respuesta (*response*), normalmente con datos en formato JSON y un código de estado HTTP.

Las APIs conectan aplicaciones, bases de datos, servicios cloud y modelos de inteligencia artificial. Permiten, por ejemplo, solicitar un resumen a un servicio de IA o iniciar un proceso de datos sin tener que construir toda esa funcionalidad desde cero.

## Conceptos esenciales

- **Endpoint:** URL de una funcionalidad de la API.
- **Request:** petición y datos que el cliente envía.
- **Response:** resultado que devuelve el servicio.
- **JSON:** formato habitual para intercambiar datos.
- **API key:** credencial que puede utilizarse para autenticar solicitudes y controlar el acceso.

Las APIs REST suelen utilizar estos métodos HTTP:

| Método | Uso habitual |
| --- | --- |
| `GET` | Consultar información |
| `POST` | Crear información o ejecutar una acción |
| `PUT` | Actualizar información |
| `DELETE` | Eliminar información |

Algunos códigos de respuesta comunes son `200` (correcto), `201` (recurso creado), `401` (falta autorización), `404` (recurso no encontrado), `422` (datos no válidos) y `500` (error interno del servidor).

## Ejemplos incluidos

- **`Test_APIs.py` y `Fast_API_demo.py`:** ejemplo de una API creada con FastAPI. El endpoint `POST /summarize` recibe texto en JSON, lo envía a Ollama y devuelve un resumen. `Test_APIs.py` hace una petición local a ese endpoint.
- **`AWS_API_demo.py`:** ejemplo de consumo de una API desplegada en AWS. Comprueba su estado, consulta archivos y envía contenido para guardarlo en S3.
- **`Lunch & Learn - APIs Vol1.pptx`:** presentación de apoyo con el contenido de la sesión.

## Ejecutar la demo local de FastAPI

Necesitas Python, [Ollama](https://ollama.com/) en ejecución y el modelo `llama3` disponible localmente. Desde la raíz del repositorio:

```bash
pip install -r requirements.txt
ollama pull llama3:8b
python -m uvicorn Fast_API_demo:app --reload
```

Con el servidor ejecutándose, abre otra terminal y ejecuta:

```bash
python Test_APIs.py
```

La API estará disponible localmente en `http://127.0.0.1:8000`. FastAPI también proporciona documentación interactiva en `http://127.0.0.1:8000/docs`.

## Buenas prácticas: validación y pruebas

La presentación también introduce cómo fortalecer una API con **Pydantic**, para validar los datos de entrada, y **PyTest**, para comprobar automáticamente el comportamiento del código antes de llevarlo a producción. La validación ayuda a rechazar datos incorrectos; las pruebas ayudan a detectar errores y a mantener el comportamiento esperado.

> Una API es el mecanismo que permite que aplicaciones, servicios cloud e inteligencia artificial hablen entre sí. Aprender APIs significa poder conectar sistemas, automatizar procesos y aprovechar servicios externos sin construir todo desde cero.
