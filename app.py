import os

from flask import Flask
from summa.summarizer import summarize
from summa import keywords
from flask import g, request

def factory():
    app = Flask(__name__, static_url_path='/static')
    app.url_map.strict_slashes = False
    return app


app = factory()

@app.route('/summary', methods = ['POST'])
def summary():
    return summarize(request.data.decode('utf-8'))

@app.route('/keyword', methods = ['POST'])
def keyword():
    return keywords.keywords(request.data.decode('utf-8'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

