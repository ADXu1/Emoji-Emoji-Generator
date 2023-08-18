from flask import Flask, render_template, request
import random

app = Flask(__name__)

emojis = {
    'happy': '😄',
    'sad': '😢',
    'love': '❤️',
    'cool': '😎',
    'laugh': '😂',
    'cry': '😭',
    'angry': '😠',
    'confused': '😕',
    'thumbs_up': '👍',
    'thumbs_down': '👎',
    # Add more keywords and emojis here
}

def generate_emoji_sentence(keywords):
    selected_emojis = [emojis[keyword] for keyword in keywords if keyword in emojis]
    if selected_emojis:
        return ' '.join(selected_emojis)
    else:
        return "No matching emojis found for the given keywords."

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        keywords = request.form['keywords'].lower().split()
        result = generate_emoji_sentence(keywords)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
