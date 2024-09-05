import psycopg2
import logging
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO)

@contextmanager
def connect_to_db():
    try:
        conn_string = "host='postgres_db' dbname='shopperdb' user='shopperdbuser' password='bgdata3.0'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        yield (conn, cursor)
    except (Exception, psycopg2.DatabaseError) as e:
        logging.error(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()