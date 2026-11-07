from sqlalchemy import text
from db import get_connection

engine = get_connection()

try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database()")
        )

        print(f"Connected to database: {result.scalar_one()}")
except Exception as e:
    print(f"Failed to connect to the database: {e}")
finally:
    engine.dispose()

    