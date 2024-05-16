import psycopg2
import os


def do_sql(sql, data=None):
    host = "localhost"
    database = "randomSQL"
    user = "postgres"  # os.environ["DB_USERNAME"]
    password = "postgres"  # os.environ["DB_PASSWORD"]

    try:
        conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        cur = conn.cursor()

        if data:
            cur.execute(sql, data)
        else:
            cur.execute(sql)

        conn.commit()

        try:
            output = cur.fetchall()
        except psycopg2.ProgrammingError:  # No data to fetch
            output = None

        cur.close()
        conn.close()
        return output

    except psycopg2.Error as e:
        print(f"SQL error: {e}")
        if conn:
            conn.rollback()
        cur.close()
        conn.close()
        return None
