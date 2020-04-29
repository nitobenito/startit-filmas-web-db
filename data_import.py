import os
import psycopg2
import csv


# Iegūstam DB informāciju no vides mainīgajiem
# lai nebūtu jāglabā parole publiski pieejama
ELEPHANT_HOST = os.getenv("ELEPHANT_HOST")
ELEPHANT_NAME = os.getenv("ELEPHANT_NAME")
ELEPHANT_PASSWORD = os.getenv("ELEPHANT_PASSWORD")

# Pieslēgums datubāzei izveidots un pieejams globāli
dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)


def parbauda_db_savienojumu():
    """Pārbauda pieslēgumu datubāzei
    
    Returns:
        string -- tekstu ar datubāzes versiju
    """
    # saformatē pieslēgšanās parametrus
    dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)
    # izveido pieslēgumu
    conn = psycopg2.connect(dsn)
    # izveido kursoru
    cur = conn.cursor()
    # aizsūta kursoram SQL vaicājumu
    cur.execute("SELECT version();")
    # pieprasa no kursora atbildi
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    # aizver kursoru
    cur.close()
    # aizver peislēgumu daubāzei
    conn.close()
    return result


def veido_vd_tabulu():
    """ 
    Izveido vārdadienu tabulu ar indeksiem uz visām kolonnām meklēšanai
    """
    conn = psycopg2.connect(dsn)
    c = conn.cursor()
    #c.execute("""DROP TABLE vardadienas;""")
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


def piepilda_vd_tabulu():
    conn = psycopg2.connect(dsn)
    c = conn.cursor()
    sql = "INSERT INTO vardadienas VALUES(%s, %s, %s)"
    
    vardu_dati = [] 
    with open("vardi.csv", "r") as f:
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


def vd_vaicajums(sql):
    try:
        conn = psycopg2.connect(dsn)
        c = conn.cursor()
        c.execute(sql)
        print(sql)
        c.close()
        conn.commit()
        return c.rowcount
    except:
        return False


print(parbauda_db_savienojumu())

# print(veido_vd_tabulu())

# print(vd_vaicajums("SELECT vards FROM vardadienas;"))

# print(piepilda_vd_tabulu("dati/vardadienas.txt"))

# print(vd_vaicajums("SELECT vards FROM vardadienas;"))
