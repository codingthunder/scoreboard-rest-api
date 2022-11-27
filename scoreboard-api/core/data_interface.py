import json
import io
import os
from .models import Score

#TODO: This is very, very, very gross. But I had a deadline to turn this in. I plan to make this muuuuch better as I continue to make this work.

file_path = '.\data.json'
try:
    with open(file_path) as i:
        print("json File exists.")
except:
    with open(file_path, 'w') as i:
        print('The json file is created')

def level_hi_score(level_id : str, limit : int = 10) -> list[Score]:
    """TODO: Actually filter based on high score. Don't use json."""
    #all_data = Score.parse_file_as(list[Score],file_path)
    f = open (file_path)

    data = json.load(f)

    f.close()

    res : list[Score] = []

    for x in data:
        
        res.append(Score.parse_raw(data[x]))
    

    return res

def submit_hi_score(level_id : str, user_id : str, score : int):
    f = open(file_path)

        

    full_data = {}

    try:
        full_data = json.load(f)
    except:
        pass

    f.close()
    score_id = level_id + user_id
    if score_id in full_data:
        old_value = Score.parse_raw(full_data[score_id])
        if (old_value.score < score):
            full_data[score_id] = Score(id=score_id,level_id=level_id,user_id=user_id,score=score).json()
    else:
        full_data[score_id] = Score(id=score_id,level_id=level_id,user_id=user_id,score=score).json()

    f = open(file_path,'w')
    json.dump(full_data,f)
    f.close()

    return True