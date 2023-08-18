from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

import random

# ...

emojis = {
    'happy': '😄',
    'sad': '😢',
    'love': '❤️',
    # Add more keywords and emojis here
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        keywords = request.form['keywords'].lower().split()
        selected_emojis = [emojis[keyword] for keyword in keywords if keyword in emojis]
        if selected_emojis:
            result = ' '.join(selected_emojis)
        else:
            result = "No matching emojis found for the given keywords."
    return render_template('index.html', result=result)
