import datetime, calendar
import os
import psycopg2
from flask import Flask, g, render_template
import data

# Iegūstam DB informāciju no vides mainīgajiem
# lai nebūtu jāglabā parole publiski pieejama
ELEPHANT_HOST = os.getenv("ELEPHANT_HOST")
ELEPHANT_NAME = os.getenv("ELEPHANT_NAME")
ELEPHANT_PASSWORD = os.getenv("ELEPHANT_PASSWORD")

# Pieslēgums datubāzei izveidots un pieejams globāli
dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)

app = Flask('app')


@app.route('/')
def index_lapa():
    return render_template('index.html')


@app.route('/healthcheck')
def hc():
    return "OK"


# vardadienu routes
@app.route('/vd/<vards>')
def vd_kad(vards):
    atbilde = data.varda_diena(vards)
    print(type(atbilde))
    resultats = {"vards": atbilde[0], "m": calendar.month_name[atbilde[2]].lower(), "d": atbilde[1]}
    return render_template('vardadienas.html', vardi=[resultats])


@app.route('/vd/menesis/<menesis>')
def vd_diena(menesis):
    atbilde = data.menesa_vardi(menesis)
    resultats = []
    for v in atbilde:
        resultats.append({"vards": v[0], "m": calendar.month_name[v[2]].lower(), "d": v[1]})
    return render_template('vardadienas.html', vardi=resultats)



@app.route('/vd/sodien')
def vd_sodien():
    sodiena = datetime.date.today()
    atbilde = data.diena(sodiena.month, sodiena.day)
    resultats = []
    for v in atbilde:
        resultats.append({"vards": v[0], "m": "", "d": ""})
    return render_template('vardadienas.html', vardi=resultats)


@app.route('/vd/rit')
def vd_rit():
    sodiena = datetime.date.today() + datetime.timedelta(days=1)
    atbilde = data.diena(sodiena.month, sodiena.day)
    resultats = []
    for v in atbilde:
        resultats.append({"vards": v[0], "m": "", "d": ""})
    return render_template('vardadienas.html', vardi=resultats)


def connect_db():
    """Connects to the database."""
    conn = psycopg2.connect(dsn)
    return conn


def get_db():
    if 'db' not in g:
        g.db = connect_db()
    return g.db


@app.teardown_appcontext
def close_db(error):
    """Close the db connection whe the current request ends
    """
    db_conn = g.pop('db', None)

    if db_conn is not None:
        db_conn.close()


if __name__ == '__main__':
  app.run(threaded=True, port=5000, debug=True)
