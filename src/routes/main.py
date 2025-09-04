from src.sys import app

@app.get("/")
def default():
    return {"Hello": "World"}

