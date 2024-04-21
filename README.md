# AdditionalAI
Add your own AI to your website using this Additional AI feature

## WHY USE ADDITIONAL AI?
The problem with large websites /info-sites is that it gets difficult to navigate through them ,or knowing about it's details can be difficult ,as well as time consuming.In such a case, additional AI helps solve these problems by directly answering the questions of the user, related to the website.
Implementing them in local languages will help even laymen users ,to easily access required features.

## Usage:-
To implement this in any website, the user just needs to add the following piece of code ,as a plug-in ,and easily train the model, according to the website's content.

# HTML code:

``` html

    <div class="floating-icon">
        <button class="fb"><img class="icon" src="{{url_for('static', filename='icon.jpg')}}"></button>
        <form action=""></form>

        <div class="chat-box">
            <div class="chat-messages" style="height: 80%; overflow-y: scroll;"></div>
            <textarea class="chat-input" style="width: 100%; height: 20%;"></textarea>
        </div>

        <!-- <script>...</script> -->

    </div>

```

# CSS code:

``` CSS
.floating-icon {
    position: fixed;
    bottom: 20px;
    right: 20px;
}
.fb {
    background-color: #ccd2cc;
    color: white;
    border: none;
    border-radius: 50%;
    padding: 15px;
    font-size: 15px;
    cursor: pointer;
    box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
}



.icon {
    border-radius: 50%;
    size-adjust: 40;
    width: 40px;
    height: 40px;
}

.window {
    display: block;
    position: fixed;
    z-index: 1;
    bottom: 80px;
    right: -330px;
    width: 300px;
    background-color: hsla(260, 83%, 54%, 0.747);
    border: 1px solid #888;
    padding: 20px;
    transition: right 0.3s;
}

.window form {
    margin-bottom: 10px;
}

.chat-box {
    display: none;
    position: fixed;
    bottom: 110px;
    right: 0;
    width: 300px;
    height: 400px;
    border: 1px solid black;
    padding: 10px;
    background-color: white;
}
```
# python code:

``` python
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

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

The developer updates the above questions in the code,or adds new ones, based on their website.Otherwise, the bot is also linked to llama2 chatbot and hence, it can answer general questions too.

