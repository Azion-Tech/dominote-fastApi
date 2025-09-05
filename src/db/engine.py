from sqlmodel import create_engine
from .env import db_host, db_port, db_name, db_password

sql_engine = create_engine(f"postgresql://:{db_password}@{db_host}:{db_port}/{db_name}")
