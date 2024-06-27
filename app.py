import flask
from flask import Flask, render_template_string
app = Flask(__name__)

dog_gifs = [
    "https://media.giphy.com/media/mCRJDo24UvJMA/giphy.gif",
    "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif",
    "https://media.giphy.com/media/jpbnoe3UIa8TU8LM13/giphy.gif"
]

@app.route('/')
def index():
    gifs = ''.join([f'<img src="{url}" alt="Dog gif">' for url in dog_gifs])
    return render_template_string(f"<h1>Dog GIFs</h1>{gifs}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


