from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Get the background color from the environment variable, default to red
    background_color = os.getenv('APP_COLOR', 'red')
    return f'<html><body style="background-color: {background_color};"><h1>Hello, World!</h1></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
