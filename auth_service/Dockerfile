FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY auth_service.py ./
CMD ["python", "auth_service.py"]
EXPOSE 5001 