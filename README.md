# Proyecto Microservicios

## Descarga del modelo entrenado

El archivo `trained_model.pkl` puede descargarse desde: [Google Drive](https://drive.google.com/drive/folders/1tu9d1D3OZlxETSOzsXqsqJge6QrvP3xu?usp=drive_link)

## Descripción general

Este proyecto implementa una arquitectura de microservicios para una aplicación modular y escalable. El objetivo principal es determinar la similitud de datos de propiedades enviadas por los usuarios, aplicando un modelo de machine learning (ML) entrenado para este fin. Cada microservicio cumple una función específica y se comunica con los demás a través de HTTP y servicios compartidos como PostgreSQL y Redis.

### Servicios principales

- **auth_service**: Gestiona la autenticación y autorización de usuarios. Utiliza PostgreSQL para almacenar usuarios y Redis para gestionar sesiones y tokens.
- **model_service**: Expone un modelo de similitud basado en machine learning. Recibe peticiones autenticadas, procesa datos y responde con resultados del modelo. Utiliza Redis para cachear resultados frecuentes. **Requiere el archivo `trained_model.pkl` en la carpeta `model_service`**
- **logging_service**: Registra eventos y logs de la aplicación en una base de datos PostgreSQL dedicada.
- **cache_service**: Proporciona una capa de cacheo adicional para acelerar respuestas de otros servicios, usando Redis.

### Flujo de funcionamiento

1. Un usuario se autentica a través de `auth_service`.
2. El token de autenticación se almacena en Redis.
3. El usuario realiza una petición a `model_service`, que valida el token con `auth_service` y procesa la solicitud.
4. Los resultados pueden ser cacheados por `cache_service` y los eventos importantes se registran en `logging_service`.

## Estructura de servicios

Cada microservicio cuenta con su propio `requirements.txt` y `Dockerfile` para facilitar la construcción y despliegue.

- **auth_service**: Flask, Redis, PostgreSQL
- **model_service**: Flask, Redis, modelo ML serializado en `trained_model.pkl`
- **logging_service**: Flask, PostgreSQL
- **cache_service**: Flask, Redis

## Inicialización de la base de datos

La inicialización de la base de datos PostgreSQL es automática. Los scripts SQL ubicados en `auth_service/init_db.sql` y `logging_service/init_db.sql` se ejecutan automáticamente al levantar el contenedor de postgres.

No es necesario ejecutar comandos manuales para inicializar la base de datos.

## Cómo levantar el proyecto:

1. Clonar el repositorio
2. Asegúrate de colocar el archivo `trained_model.pkl` en la carpeta `model_service`.
3. Ejecutar:

```bash
docker-compose up --build
```

4. Correr los tests:

```bash
cd tests
pytest test_api.py
```

## Ejemplo de uso de la API

- **Autenticación:**
  - `POST /login` en `auth_service` con usuario y contraseña para obtener un token.
- **Predicción:**
  - `POST /service` en `model_service` enviando datos y el token en el header.
- **Logs:**
  - `GET /logs` en `logging_service` para consultar eventos registrados.


