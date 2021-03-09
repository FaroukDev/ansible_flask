import logging
import os
import sys


from flask import (
    Flask,
    jsonify,
    render_template,
    request
)
from logger import log
import db

logging.basicConfig(filename="LOG_elearning.log",
                    filemode="a",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    print('Connexion flask :')
    app.run(host='0.0.0.0', port=4000, debug=True)