import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

db_name = os.getenv("DB_NAME")
db_password = os.getenv("DB_PASSWORD")
conn = psycopg2.connect(f"dbname= {db_name} password={db_password}")

def get_data_from_table(table_name: str):
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()
