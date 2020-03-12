import psycopg2
from flask import Flask


app = Flask('app')


@app.route('/')
def index_lapa():
  return "OK"


@app.route('/dbtest')
def db_test():
    dsn = "host={} dbname={} user={} password={}".format("balarama.db.elephantsql.com", "dwtgtufa", "dwtgtufa", "DzmzOK0aSTWv-kBKOCtzuxqYfyLwZ6Bf")
    print(dsn)
    conn = psycopg2.connect(dsn)
    print(conn)
    cur = conn.cursor()
    print(cur)
    cur.execute("SELECT version();")
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    cur.close()
    conn.close()
    return result

if __name__ == '__main__':

  # Threaded option to enable multiple instances for multiple user access support
  app.run(threaded=True, port=5000, debug=True)
