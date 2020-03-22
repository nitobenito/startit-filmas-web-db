from main import get_db


def get_one(sql, params):
    conn = get_db()
    c = conn.cursor()
    c.execute(sql, params)
    atbilde = c.fetchone()
    print("Vaicājums:\n{}\nAtbilde: {}".format(c.query, atbilde))
    c.close()
    return(atbilde)


def get_all(sql, params):
    conn = get_db()
    c = conn.cursor()
    c.execute(sql, params)
    atbilde = c.fetchall()
    print("Vaicājums:\n{}\nAtbilde: {}".format(c.query, atbilde))
    c.close()
    return(atbilde)


