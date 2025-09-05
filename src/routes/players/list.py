from src.sys import app
from src.db import get_data_from_table, Players

@app.get("/players/list")
def get_list_of_players():
    """
    Endpoint to get a list of players from the database.
    """
    try:
        players = get_data_from_table(Players)
        return {"players": players}
    except Exception as e:
        return {"error": str(e)}
