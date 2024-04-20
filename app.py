from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        question = request.form.get('question')
        data = {
            "model": "orca-mini",
            "prompt": str(question)
        }

        response = requests.post("http://127.0.0.1:11434/api/generate", json=data, stream=True)

        if 'application/x-ndjson' in response.headers.get('Content-Type'):
            lines = response.text.splitlines()
            responses = [json.loads(line) for line in lines if line]
            paragraph = "".join([resp['response'] for resp in responses if 'response' in resp])

            return paragraph

        # return render_template('index.html', paragraph)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)