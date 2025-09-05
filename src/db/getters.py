
from sqlmodel import select, Session, SQLModel
from .engine import sql_engine

"""Retrieve data from the Players table in the database."""
def get_data_from_table(sql_model: SQLModel):
    session = Session(sql_engine)
    return session.exec(select(sql_model)).all()
