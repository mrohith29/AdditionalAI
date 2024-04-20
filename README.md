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

#image>img {
    border-radius: 50%;
    padding-right: 0%;
    text-align: right;
    float: right;
    height: 100%;
    width: 20%;
}


.floating-icon {
    position: fixed;
    bottom: 20px;
    right: 20px;
}
/* onclick="this.style.backgroundColor='blue' */
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
        if question == 'what is this website?':
            return 'This is a simple portfolio webpage with cool nav bar and editable content.'
        elif question == 'who am i?':
            return 'since you are using the website i might think that you are a user using this website for your own purpose.'
        elif question == 'what are the default skills provided in this webpage':
            return 'Python, Java, C, HTML, CSS, JavaScript, SQL'
        elif question == '':
            return 'please enter a valid question'
        elif question == 'Who is the founder of Additional AI':
            return 'This feature is developed by Mariyala Rohith and Gunuganti Sathvik behalf of their hackathon project'
        elif question == 'How to use this website?':
            return 'This is a sample page for webfolio and it can be used for creating a portfolio website by adding your information in the respective places'
        elif question == 'What is your name?':
            return 'My name is [Your Name].'
        elif question == 'What is your background?':
            return 'I have a background in [Your Background].'
        elif question == 'What is your experience?':
            return 'I have experience in [Your Experience].'
        elif question == 'What are your skills?':
            return 'My skills include [Your Skills].'
        elif question == 'What projects have you worked on?':
            return 'I have worked on projects such as [Your Projects].'
        elif question == 'What is your education?':
            return 'I have a degree in [Your Degree] from [Your University].'
        elif question == 'How can I contact you?':
            return 'You can contact me at [Your Email Address].'
        elif question == 'What services do you offer?':
            return 'I offer services such as [Your Services].'
        elif question == 'What is your work philosophy?':
            return 'My work philosophy is [Your Philosophy].'
        elif question == 'What languages do you speak?':
            return 'I speak [Your Languages].'
        elif question == 'What is your availability?':
            return 'I am currently [Your Availability].'
        elif question == 'Do you have any certifications?':
            return 'Yes, I have certifications in [Your Certifications].'
        elif question == 'What is your rate?':
            return 'My rate is [Your Rate].'
        elif question == 'Where are you located?':
            return 'I am located in [Your Location].'
        elif question == 'What programming languages do you know?':
            return 'I am proficient in [Your Programming Languages].'
        elif question == 'What frameworks do you use?':
            return 'I have experience with [Your Frameworks].'
        elif question == 'What is your preferred development environment?':
            return 'I prefer to work in [Your Preferred Development Environment].'
        elif question == 'What is your approach to problem solving?':
            return 'My approach to problem solving is [Your Approach].'
        elif question == 'What is your greatest achievement?':
            return 'One of my greatest achievements is [Your Achievement].'
        elif question == 'What are your career goals?':
            return 'My career goals include [Your Goals].'
        elif question == 'What industries have you worked in?':
            return 'I have worked in the following industries: [Your Industries].'
        elif question == 'What is your process for testing and finding bugs in your work?':
            return 'My process for testing and finding bugs is [Your Process].'
        elif question == 'What is your approach to learning new technologies?':
            return 'My approach to learning new technologies is [Your Approach].'
        elif question == 'What is your favorite project you\'ve worked on and why?':
            return 'My favorite project is [Your Project], because [Your Reason].'
        elif question == 'Who are you?':
            return 'I am the AI assistant for this website' 
        
        else:
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

