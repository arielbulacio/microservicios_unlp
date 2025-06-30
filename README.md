# Proyecto Microservicios

## Estructura de servicios

Cada microservicio cuenta con su propio `requirements.txt` y `Dockerfile` para facilitar la construcción y despliegue.

- **auth_service**: Flask, Redis, PostgreSQL
- **model_service**: Flask, Redis, Tensorflow. **Requiere el archivo `modelo_similitud.h5` en la carpeta `model_service`**
- **logging_service**: Flask, PostgreSQL
- **cache_service**: Flask, Redis

## Inicialización de la base de datos

La inicialización de la base de datos PostgreSQL es automática. Los scripts SQL ubicados en `auth_service/init_db.sql` y `logging_service/init_db.sql` se ejecutan automáticamente al levantar el contenedor de postgres.

No es necesario ejecutar comandos manuales para inicializar la base de datos.

## Cómo levantar el proyecto:

1. Clonar el repositorio
2. Asegúrate de colocar el archivo `modelo_similitud.h5` en la carpeta `model_service`.
3. Ejecutar:

```bash
docker-compose up --build
```

4. Correr los tests:

```bash
cd tests
pytest test_api.py
```
