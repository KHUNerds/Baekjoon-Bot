import os
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import json
import time


class Baekjoon_cralwer:
    def __init__(self):
        self.options = Options()
        self.folderPath = os.path.dirname(os.path.realpath(__file__))
        self.packed_extension_path = self.folderPath + '/extensions/anenheoccfogllpbpcmbbpcbjpogeehe.crx'
        self.options.add_extension(self.packed_extension_path)
        self.chromedriver_path = "chromedriver.exe"
        self.browser = webdriver.Chrome(self.chromedriver_path, chrome_options=self.options)
        self.problem_dict = {}

    def crawling(self):
        for page_num in range(1, 113):
            print(page_num)

            url = 'https://www.acmicpc.net/problemset?sort=solvedac_asc&page=' + str(page_num)
            self.browser.get(url)
            time.sleep(1)

            soup = BeautifulSoup(self.browser.page_source, "lxml")

            tr_list = soup.find("table", attrs={"id":"problemset"}).find("tbody").find_all("tr")

            for tr in tr_list:
                number = int(tr.find('td', attrs={"class":"list_problem_id"}).get_text())
                tier = tr.find('a').find("span", attrs={"class":"level_hidden"}).get_text()
                title = tr.find('a').get_text()
                problem_url = "https://www.acmicpc.net/problem/" + str(number)
                self.problem_dict[str(number)] = {'number':str(number), 'title':title, 'tier':tier, 'url':problem_url}
                
    def makeJson(self, problemset):
        with open('problem_set.json', 'w', encoding='utf-8') as file :
            json.dump(problemset, file, ensure_ascii=False, indent='\t')

    def run(self):
        self.crawling()
        self.makeJson(self.problem_dict)

if __name__ == '__main__':
    baekjoon = Baekjoon_cralwer()
    baekjoon.run()