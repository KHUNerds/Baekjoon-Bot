import json

with open('problem_set.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)
    
json_key_dict = list(json_data.keys())
for key in json_key_dict:
    json_data[key]['title'] = json_data[key]['title'][2:]

with open('problem_set.json', 'w', encoding='utf-8') as of :
            json.dump(json_data, of, ensure_ascii=False, indent='\t')