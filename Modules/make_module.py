import json
from random import choice


# open json file
# json file to json_data
with open("../Resource/problem_set.json", 'r', encoding='utf-8') as f:
    json_data = json.load(f)


def recommand_rand_problem() -> dict:
    json_key_list = list(json_data.keys())
    random_key = choice(json_key_list)
    return json_data[random_key]


def recommand_tier_rand_problem(tier : str) -> dict:
    '''
    tier:
    "00" : unranked
    "01" : Bronze5
    ...
    '''
    json_key_list = list(json_data.keys())
    json_tier_key_list = []
    
    for key in json_key_list:
        if(int(json_data[key]['tier']) > int(tier)):
            break
        elif(json_data[key]['tier'] == tier):
            json_tier_key_list.append(key)

    random_tier_key = choice(json_tier_key_list)
    return json_data[random_tier_key]

def find_problem(num : string) -> dict:
    '''
    num:
    "1000" ~ ....
    '''
    json_key_list = list(json_data.keys())

    if key in json_key_list:
        return json_data[num]
    else:
        return {}


if __name__ == '__main__':
    print(recommand_rand_problem())
    print(recommand_tier_rand_problem("21"))
    print(find_problem("1002"))