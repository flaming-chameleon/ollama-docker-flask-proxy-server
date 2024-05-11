from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Fetch the AI service URL from environment variables with a fallback default
AI_SERVICE_URL = os.getenv('AI_SERVICE_URL', 'http://ollama:11434')


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    # Create the full URL by appending the path to the base URL
    full_url = f"{AI_SERVICE_URL}/{path}"

    # Forward the incoming request to the AI service
    resp = requests.request(
        method=request.method,
        url=full_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    
    return jsonify({"response": resp.json()["response"]})

if __name__ == '__main__':
    # Pull the model from the AI service
    requests.post(AI_SERVICE_URL + '/api/pull', json={"name": "llama3"})
    
    app.run(host='0.0.0.0', debug=True)
