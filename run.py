from flask import Flask, render_template
import os

path = os.path.join('static', 'pictures')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/camera')
def camera():
    pictures = path = os.path.join('static', 'pictures', 'Bild.jpg')
    return render_template('camera.html', pictures=pictures)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
