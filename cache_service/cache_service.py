from flask import Flask, request, jsonify
from functools import wraps
import redis

app = Flask(__name__)
cache = redis.Redis(host='localhost', port=6379, db=0)

def cache_response(timeout=60):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            key = f"cache:{request.full_path}"
            cached = cache.get(key)
            if cached:
                return jsonify({'cached': True, 'data': cached.decode('utf-8')})
            response = f(*args, **kwargs)
            cache.setex(key, timeout, response.get_data())
            return response
        return wrapped
    return decorator

@app.route('/cached_service', methods=['GET'])
@cache_response(timeout=300)
def cached_service():
    return jsonify({'message': 'Data generada dinámicamente'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
