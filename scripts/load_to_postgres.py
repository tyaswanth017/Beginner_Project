from pathlib import Path

import pandas as pd
from sqlalchemy import text 

from db_connection.db import get_connection


#step 1: Read Cleaned CSV file
project_dir = Path(__file__).resolve().parents[1]
file_path = project_dir / "data" / "clean_orders.csv"

df = pd.read_csv(file_path)

print("Total records:", len(df))

#step 2: Validate the data
if df.empty:
    raise ValueError("CSV contains no records. Please check the file.")

if df.isna().any().any():
    raise ValueError("CSV contains missing values.")

if df['order_id'].duplicated().any():
    raise ValueError("CSV contains duplicate order_id values.")

if (df['quantity'] <= 0).any() or (df['unit_price'] < 0).any():
    raise ValueError("Invalid quantity or price")

df['order_date'] = pd.to_datetime(
    df['order_date']
).dt.date 


#step 3: Load data into PostgreSQL
engine = get_connection()

try:
    with engine.begin() as connection:

        existing_rows = connection.execute(
            text("SELECT COUNT(*) FROM orders")
        ).scalar_one()

        if existing_rows != 0:
            raise ValueError("Orders table is not empty. Load skipped.")

        df.to_sql(
            name = "orders",
            con=connection,
            if_exists="append",
            index=False
        )

    print("Data loaded successfully")

except Exception as error:
    print("An execption caught check it out!!", error)

finally:
    engine.dispose()
