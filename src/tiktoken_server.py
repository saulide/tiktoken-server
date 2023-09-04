import json
from flask import Flask, request
from flask_cors import CORS   # Import CORS
import tiktoken

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

@app.route("/tokenize", methods=['POST'])
def token_count():
    data = request.get_json()
    if not 'prompt' in data:
        return json.dumps({'tokens': []})
    
    model = "text-davinci-003"
    if 'model' in data:
        model = data['model']

    print('Model:', model)
    print('Data:', data)
    try:
        print('Getting encoding for model ' + model)
        enc = tiktoken.encoding_for_model(model)
    except:
        return json.dumps({'error': "Model not found"})
    return json.dumps({'tokens': enc.encode(data['prompt'])})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
