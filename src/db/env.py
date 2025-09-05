import os
from dotenv import load_dotenv
load_dotenv()

db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")
db_password = os.getenv("DB_PASSWORD")
