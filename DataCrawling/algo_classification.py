import os
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver

import requests
import csv
import json
import time

import env

class Baekjoon_crawler:
    def __init__(self):
        self.options = Options()
        self.folderPath = os.path.dirname(os.path.realpath(__file__))
        self.packed_extension_path = self.folderPath + '/extensions/anenheoccfogllpbpcmbbpcbjpogeehe.crx'
        self.options.add_extension(self.packed_extension_path)
        self.chromedriver_path = "/chromedriver.exe"
        self.browser = webdriver.Chrome(self.folderPath + self.chromedriver_path, chrome_options=self.options)
        self.__baekjoon_id = env.user_id
        self.__baekjoon_password = env.user_password
        self.problem_list = []

    def login(self):
        url = 'https://www.acmicpc.net/login?next=%2F'
        self.browser.get(url)
        time.sleep(1)

        id_box = self.browser.find_element_by_xpath("//*[@id='login_form']/div[2]/input")
        password_box = self.browser.find_element_by_xpath("//*[@id='login_form']/div[3]/input")
        id_box.send_keys(self.__baekjoon_id)
        password_box.send_keys(self.__baekjoon_password)
        self.browser.find_element_by_xpath("//*[@id='submit_button']").click()
        time.sleep(100)

    def crawling(self):
        url = 'https://www.acmicpc.net/problem/' + str(problem_num)
        self.browser.get(url)
        time.sleep(1)

        soup = BeautifulSoup(self.browser.page_source, "lxml")

        tr_list = soup.find("table", attrs={"id":"problemset"}).find("tbody").find_all("tr")

        for tr in tr_list:
            number = []
            number.append(tr.find('td', attrs={"class":"list_problem_id"}).get_text())
            self.problem_list.append(number)

    def run(self):
        self.login()

if __name__ == '__main__':
    baekjoon = Baekjoon_crawler()
    baekjoon.run()