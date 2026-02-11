import pyodbc
from  contextlib import contextmanager
from config import DB_DRIVER, DB_SERVER, DB_NAME, DB_TRUSTED

@contextmanager
def sql_conn():
    conn = pyodbc.connect(
        f"DRIVER={{{DB_DRIVER}}};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_NAME};"
        f"Trusted_Connection={DB_TRUSTED};"
        "TrustServerCertificate=yes;",
        autocommit=False
    )
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
