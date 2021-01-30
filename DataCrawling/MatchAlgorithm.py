from bs4 import BeautifulSoup
import requests
import json

# crowling algorithms
url = "https://www.acmicpc.net/problem/tags"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

aTags = soup.find("div", {"class": "table-responsive"}).find_all("a")

# add algorithms in list
algorithms = []
for aTag in aTags:
    
    algorithms.append([aTag.get_text(), aTag["href"]])

# add algorithms in dict
dictonary = {}
for i in range(len(algorithms)):
    if i % 2 == 1:
        dictonary[algorithms[i][0]] = {'korean':algorithms[i-1][0], 'url':"https://www.acmicpc.net" + algorithms[i-1][1]}

# add algorithms in json file
with open('match_algorithm.json', 'w', encoding='utf-8') as file :
    json.dump(dictonary, file, ensure_ascii=False, indent='\t')

