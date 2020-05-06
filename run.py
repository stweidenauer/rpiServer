from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/camera')
def camera():
    pictures = ['Bild1', 'Bild2']
    return render_template('camera.html', pictures=pictures)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
