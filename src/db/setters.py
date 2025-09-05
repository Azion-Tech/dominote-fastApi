


from sqlmodel import select, Session, SQLModel
from .engine import sql_engine

"""Retrieve data from the Players table in the database."""
def set_data_to_table(sql_model: SQLModel):
    session = Session(sql_engine)
    session.add(sql_model)
    session.commit()
