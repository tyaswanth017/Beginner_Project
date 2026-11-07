from getpass import getpass
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def get_connection():
    db_url = URL.create (
        "postgresql+psycopg",
        username="postgres",
        password= getpass("PostgresSQL password: " ),
        host="localhost",
        port=5432,
        database="sales_db"
    )

    return create_engine(db_url)
