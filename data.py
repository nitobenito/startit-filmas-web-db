import os
import psycopg2

# Iegūstam DB informāciju no vides mainīgajiem
# lai nebūtu jāglabā parole publiski pieejama
# Vienkāršam testam var nomainīt šīs vērtības pret konkrētiem lielumiem

ELEPHANT_HOST = os.getenv("	postgres://vifluamr:AOUN0ksvWTDBusvzPVxbQofcJ1H6U07O@balarama.db.elephantsql.com:5432/vifluamr")
ELEPHANT_NAME = os.getenv("vifluamr")
ELEPHANT_PASSWORD = os.getenv("AOUN0ksvWTDBusvzPVxbQofcJ1H6U07O")


def test_connection():
    """Pārbauda pieslēgumu datubāzei
    
    Returns:
        string -- tekstu ar datubāzes versiju
    """
    dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    cur.close()
    conn.close()
    return result
