from flask import Flask, render_template, request, jsonify
import requests, os

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('index.html')

@app.post('/api/run-java')
def run_java():
    data = request.get_json(silent=True) or {}
    code = data.get('code', '')
    stdin = data.get('stdin', '')
    if not isinstance(code, str) or not code.strip():
        return jsonify(error='Enter a Java program before running it.'), 400
    if len(code) > 20000 or len(stdin) > 5000:
        return jsonify(error='Code or input is too large.'), 413
    # Piston executes code in an isolated runtime. Keep this proxy server-side.
    payload = {'language': 'java', 'version': '*', 'files': [{'name': 'Main.java', 'content': code}], 'stdin': stdin, 'args': [], 'compile_timeout': 10000, 'run_timeout': 5000}
    try:
        response = requests.post('https://emkc.org/api/v2/piston/execute', json=payload, timeout=20)
        response.raise_for_status()
        result = response.json()
        return jsonify(result)
    except requests.RequestException:
        return jsonify(error='The code execution service is temporarily unavailable. Try again shortly.'), 502

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
