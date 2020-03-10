import psycopg2
from flask import Flask


app = Flask('app')


@app.route('/')
def index_lapa():
  return "OK"


@app.route('/dbtest')
def db_test():
  return db_check()


def db_check():
    dsn = "host={} dbname={} user={} password={}".format("balarama.db.elephantsql.com", "dwtgtufa", "dwtgtufa", "DzmzOK0aSTWv-kBKOCtzuxqYfyLwZ6Bf")
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    record = cur.fetchone()
    cur.close()
    conn.close()
    result = "You are connected to - " + record
    return result

if __name__ == '__main__':

  # Threaded option to enable multiple instances for multiple user access support
  app.run(threaded=True, port=5000, debug=True)
