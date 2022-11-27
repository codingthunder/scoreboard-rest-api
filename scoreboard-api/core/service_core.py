from . import data_interface as DB

from .models import Score
def level_hi_score(level_id : str, limit : int = 10) -> list[Score]:
    print("level_hi_score service called.")
    dummy_score = Score(id = "abcdef", level_id = level_id, score = "42", user_id = "scrubward")
    return DB.level_hi_score(level_id,limit)

def submit_hi_score(level_id : str, user_id : str, score : int):
    return DB.submit_hi_score(level_id=level_id, user_id=user_id,score=score)