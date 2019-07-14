#! python3 

# A simple script for navigatin the awful search menu of https://www.addic7ed.com/ using Selenium webdriver

import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s\
- %(message)s')

logging.disable(logging.CRITICAL)


def get_show_number(title):
    res = requests.get('http://www.addic7ed.com/')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for option in soup.find_all('option'):
        if option.text == title:
            return option['value']


def subtitle(title, season):
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    browser = webdriver.Firefox(firefox_binary=binary, executable_path="geckodriver.exe")
    browser.get('http://www.addic7ed.com/show/' + str(get_show_number(title)))
    browser.implicitly_wait(3)
    html_elem = browser.find_element_by_tag_name('html')
    browser.find_element_by_xpath('//*[@id="sl"]/button[%s]' % season).click()
    browser.implicitly_wait(3)
    browser.find_element_by_xpath('//*[@id="lang1"]').click()
    browser.implicitly_wait(3)
    browser.find_element_by_xpath('//*[@id="noncheck"]').click()
    browser.implicitly_wait(3)
    browser.find_element_by_xpath('//*[@id="hdcheck"]').click()
    for i in range(10):
        html_elem.send_keys(Keys.DOWN)


if __name__ == "__main__":
    subtitle('Breaking Bad', 3)