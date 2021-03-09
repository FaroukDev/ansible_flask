import logging
import os
import sys
from dotenv import load_dotenv
load_dotenv()


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
    print("hello la famix")
    



if __name__ == '__main__':
    print('Connexion flask :')
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True)