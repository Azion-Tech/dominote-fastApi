from sqlmodel import SQLModel, Field

class Players(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(nullable=False)
    score: int | None = Field(default=0)
    wins: int | None = Field(default=0)
    games_played: int | None = Field(default=0)
