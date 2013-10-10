import sqlite3


CALLBACK_DB = 'call_back.db'


def sql3_query(qry, params):
    ret = []
    try:
        conn = sqlite3.connect(CALLBACK_DB)
        cursor = conn.execute(qry, params)

        for row in cursor:
            ret.append(row)

        return ret[0][0]

    except Exception, e:
        print str(e)


def sql3_insert(qry, params):
    try:
        conn = sqlite3.connect(CALLBACK_DB)
        c = conn.cursor()
        c.execute(qry, params)
        conn.commit()

    except Exception, e:
        print str(e)


def get_orders(uid):
    command = ""
    command = sql3_query('SELECT command from orders where uid=?', (uid,))

    return command
