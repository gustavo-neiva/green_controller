from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


def run_flask():
    app.run(debug=True, host='0.0.0.0', use_reloader=False, threaded=True)
