from flask import Flask, request, jsonify
import redis
import psycopg2

app = Flask(__name__)
cache = redis.Redis(host='localhost', port=6379, db=0)

conn = psycopg2.connect("dbname=api_db user=admin password=secret host=postgres")
cursor = conn.cursor()

def verify_api_key(api_key):
    cached = cache.get(api_key)
    if cached:
        return cached.decode('utf-8')
    cursor.execute("SELECT tipo FROM api_keys WHERE key=%s", (api_key,))
    result = cursor.fetchone()
    if result:
        cache.set(api_key, result[0], ex=3600)
        return result[0]
    return None

@app.route('/auth', methods=['GET'])
def authenticate():
    api_key = request.headers.get('Authorization')
    if not api_key:
        return jsonify({'error': 'API Key requerida'}), 401
    user_type = verify_api_key(api_key)
    if not user_type:
        return jsonify({'error': 'API Key inválida'}), 403
    return jsonify({'message': 'Autenticación exitosa', 'tipo': user_type})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
