FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY cache_service.py ./
CMD ["python", "cache_service.py"]
EXPOSE 5004 