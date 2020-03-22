import csv
import os
import psycopg2
from db import get_one, get_all


# Iegūstam DB informāciju no vides mainīgajiem
# lai nebūtu jāglabā parole publiski pieejama
ELEPHANT_HOST = os.getenv("ELEPHANT_HOST")
ELEPHANT_NAME = os.getenv("ELEPHANT_NAME")
ELEPHANT_PASSWORD = os.getenv("ELEPHANT_PASSWORD")

# Pieslēgums datubāzei izveidots un pieejams globāli
dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)


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


def vd_vaicajums(sql):
    try:
        conn = psycopg2.connect(dsn)
        c = conn.cursor()
        c.execute(sql)
        skaits = c.rowcount
        c.close()
        conn.commit()
        return skaits
    except:
        return False


def create_vd_table():
    """ 
    Izveido vārdadienu tabulu ar indeksiem uz visām kolonnām meklēšanai
    """
    conn = psycopg2.connect(dsn)
    c = conn.cursor()
    c.execute("""DROP TABLE vardadienas;""")
    c.execute("""CREATE TABLE vardadienas
                (vards TEXT COLLATE "lv-x-icu" PRIMARY KEY, diena INT NOT NULL, menesis INT NOT NULL);""")
    c.execute("""CREATE INDEX d1 ON vardadienas(diena);""")
    c.execute("""CREATE INDEX m1 ON vardadienas(menesis);""")
    skaits = c.rowcount
    print(skaits)
    c.close()
    conn.commit()
    conn.close()
    return "OK"


def piepilda_vd_tabulu(datne):
    conn = psycopg2.connect(dsn)
    c = conn.cursor()
    sql = "INSERT INTO vardadienas VALUES(%s, %s, %s)"
    
    vardu_dati = [] 
    with open(datne, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            vardu_dati.append(line)
    
    c.executemany(sql, vardu_dati)
    skaits = c.rowcount
    print(skaits)
    conn.commit()
    c.close()
    conn.close()
    return "OK"


def varda_diena(vards):
    sql = "SELECT * FROM vardadienas WHERE vards=%s"
    t = (vards,)
    atbilde = get_one(sql, t)
    return atbilde


def menesa_vardi(menesis):
    sql = "SELECT * FROM vardadienas WHERE menesis=%s"
    m = (menesis,)
    atbilde = get_all(sql, m)
    return atbilde


def diena(menesis, diena):
    sql = "SELECT * FROM vardadienas WHERE menesis=%s AND diena=%s"
    atbilde = get_all(sql, (menesis, diena))
    return atbilde


def statistika(menesis='visi'):
    if menesis == 'visi':
        c.execute('''SELECT menesis, diena, count(vards) from vardadienas GROUP BY menesis, diena ORDER BY menesis ASC, diena ASC''')
    else:
        c.execute('SELECT menesis, diena, count(vards) from vardadienas WHERE menesis=? GROUP BY menesis, diena ORDER BY menesis ASC, diena ASC', (menesis,))
    return c.fetchall()
