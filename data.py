import os
import psycopg2


ELEPHANT_HOST = os.getenv("ELEPHANT_HOST", "balarama.db.elephantsql.com")
ELEPHANT_NAME = os.getenv("ELEPHANT_NAME")
ELEPHANT_PASSWORD = os.getenv("ELEPHANT_PASSWORD")


def test_connection():
    dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    cur.close()
    conn.close()
    return result