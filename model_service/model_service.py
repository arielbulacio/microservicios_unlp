from flask import Flask, request, jsonify
import redis
import tensorflow as tf

app = Flask(__name__)
cache = redis.Redis(host='localhost', port=6379, db=0)
model = tf.keras.models.load_model('modelo_similitud.h5')

def preprocess(graph_1, graph_2):
    return [[0.5]]  # Simulación de preprocesamiento

def predict_similarity(graph_1, graph_2):
    input_data = preprocess(graph_1, graph_2)
    prob = model.predict(input_data)
    return float(prob[0][0])

@app.route('/service', methods=['POST'])
def process_graphs():
    api_key = request.headers.get('Authorization')
    if not api_key:
        return jsonify({'error': 'No autorizado'}), 403

    data = request.json.get("inputs", [])
    if len(data) != 2:
        return jsonify({'error': 'Debe enviar exactamente dos conjuntos de propiedades'}), 400

    probability = predict_similarity(data[0], data[1])
    return jsonify({'probabilidad': probability})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
