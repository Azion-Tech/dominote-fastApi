from src.sys import app
from src.db import set_data_to_table, Players

@app.post("/players/register")
def register_player(player: Players):
    """
    Endpoint to register a new player in the database.
    """
    try:
        set_data_to_table(player)
        return {"message": "Player registered successfully"}
    except Exception as e:
        if str(e).find("UNIQUE constraint failed"):
            return {"error": "Player with this name already exists"}
        else: 
            return {"error": str(e)}
