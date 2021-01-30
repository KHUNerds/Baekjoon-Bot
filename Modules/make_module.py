import json
from random import choice


# open json file
# json file to json_data
with open("./Resources/problem_set.json", 'r', encoding='utf-8') as f:
    json_data = json.load(f)

class Problem:
    def __init__(self, number, title, tier, url):
        self.number = number
        self.title = title
        self.tier = tier
        self.url = url

    def get_number(self):
        return self.number

    def get_title(self):
        return self.title

    def get_tier(self):
        return self.tier

    def get_url(self):
        return self.url

def recommand_rand_problem() -> Problem:
    json_key_list = list(json_data.keys())
    random_key = choice(json_key_list)
    
    number = json_data[random_key]["number"]
    title = json_data[random_key]["title"]
    tier = json_data[random_key]["tier"]
    url = json_data[random_key]["url"]

    problem = Problem(number, title, tier, url)
    return problem


def recommand_tier_rand_problem(tier : str) -> Problem:
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

    number = json_data[random_tier_key]["number"]
    title = json_data[random_tier_key]["title"]
    tier = json_data[random_tier_key]["tier"]
    url = json_data[random_tier_key]["url"]

    problem = Problem(number, title, tier, url)
    return problem

def find_problem(num : str) -> dict:
    '''
    num:
    "1000" ~ ....
    '''

    try:
        number = json_data[num]["number"]
        title = json_data[num]["title"]
        tier = json_data[num]["tier"]
        url = json_data[num]["url"]

        problem = Problem(number, title, tier, url)
        return problem
    except:
        return None


if __name__ == '__main__':
    print(recommand_rand_problem().get_number())
    print(recommand_tier_rand_problem("21").get_number())
    print(find_problem("1339").get_number())