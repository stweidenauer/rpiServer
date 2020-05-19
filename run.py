import os

from flask import Flask, render_template

path_to_pictures = os.path.join('static', 'pictures')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/camera')
def camera():
    pictures = []
    # path ist cwd
    # erstellt eine Liste aller Pfadangaben,
    # aller Bilder im Verzeichnis /static/pictures
    for picture in os.listdir(path_to_pictures):
        pictures.append(os.path.join(path_to_pictures, picture))
    return render_template('camera.html', pictures=pictures)


@app.route('/LH-Wiki')
def lhwiki():
    return render_template('lhwiki.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
