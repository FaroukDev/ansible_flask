from flask import Flask, request, render_template

from flask import jsonify

import psycopg2

app = Flask(__name__)


@app.route('/')
def hello():
    return "Bienvenue la famille"


@app.route('/test')
def showData():
    try:
        conn = psycopg2.connect(host='localhost',
                                    user='farouk',
                                    database='postgres',
                                    password='pw123')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        print("ok")
        myresult = cursor.fetchall()
        #fermeture de la base de donnée
        conn.close()
        return jsonify(myresult)
    except Exception as e :
        print("Error :", e) 

@app.route('/id')
def showId():
    conn = psycopg2.connect(host='localhost',
                                    user='farouk',
                                    database='postgres',
                                    password='pw123')
    cursor = conn.cursor()
    cursor.execute("SELECT currval('users_id_seq')")
    myresult = cursor.fetchall()
    #fermeture de la base de donnée
    conn.close()
    return jsonify(myresult)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)