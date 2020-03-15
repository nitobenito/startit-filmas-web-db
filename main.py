import psycopg2
from flask import Flask
import data


app = Flask('app')


@app.route('/')
def index_lapa():
  return data.test_connection()


@app.route('/healthcheck')
def hc():
    return "OK"


if __name__ == '__main__':

  # Threaded option to enable multiple instances for multiple user access support
  app.run(threaded=True, port=5000, debug=True)
