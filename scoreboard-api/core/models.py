from pydantic import BaseModel

class Score(BaseModel):
    id : str
    level_id : str
    score : int
    user_id : str

