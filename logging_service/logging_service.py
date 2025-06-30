from flask import Flask, request
import psycopg2
import time

app = Flask(__name__)
conn = psycopg2.connect("dbname=api_db user=admin password=secret host=postgres")
cursor = conn.cursor()

def log_request(endpoint, api_key, duration):
    cursor.execute("INSERT INTO logs (endpoint, api_key, duration) VALUES (%s, %s, %s)", (endpoint, api_key, duration))
    conn.commit()

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_request_data(response):
    duration = time.time() - request.start_time
    api_key = request.headers.get('Authorization', 'Unknown')
    log_request(request.path, api_key, duration)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
