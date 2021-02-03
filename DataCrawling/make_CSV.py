import os
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver

import requests
import csv
import json
import time


# To make CSV
class Baekjoon_crawler:
    def __init__(self):
        self.options = Options()
        self.folderPath = os.path.dirname(os.path.realpath(__file__))
        self.packed_extension_path = self.folderPath + '/extensions/anenheoccfogllpbpcmbbpcbjpogeehe.crx'
        self.options.add_extension(self.packed_extension_path)
        self.chromedriver_path = "/chromedriver.exe"
        self.browser = webdriver.Chrome(self.folderPath + self.chromedriver_path, chrome_options=self.options)
        self.problem_list = []

    def crawling(self):
        for page_num in range(1, 113):
            print(page_num)

            url = 'https://www.acmicpc.net/problemset?sort=solvedac_asc&page=' + str(page_num)
            self.browser.get(url)
            time.sleep(1)

            soup = BeautifulSoup(self.browser.page_source, "lxml")

            tr_list = soup.find("table", attrs={"id":"problemset"}).find("tbody").find_all("tr")

            for tr in tr_list:
                number = []
                number.append(tr.find('td', attrs={"class":"list_problem_id"}).get_text())
                self.problem_list.append(number)
                
    def makeJson(self, problemset):
        with open('problem_set.json', 'w', encoding='utf-8') as file :
            json.dump(problemset, file, ensure_ascii=False, indent='\t')

    def makeCSV(self):
        with open ('problem_number.csv', 'w', newline = '', encoding='utf-8') as f:
            writer = csv.writer(f)
            for number in range (len(self.problem_list)):
                writer.writerow(self.problem_list[number])

    def run(self):
        self.crawling()
        self.makeCSV()