import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

print()
#print("--------------get the html--------------")
url = "https://www.amazon.in/s?k=mobiles&ref=nb_sb_noss_2"
page = requests.get(url)
#print(page.text)

#print()
print("--------------parsing html--------------")
driver = webdriver.Firefox()
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
#driver.find_elements("div")
time.sleep(5)

#print(sel_soup)

print("--------------Fetching data--------------")
#result = soup.findAll("h4")
#result= driver.find_elements("div", class_ = "s-main-slot s-result-list s-search-results sg-row")
#tag = sel_soup.findAll("h2")
atag = sel_soup.h2.a
#result = BeautifulSoup.findAll("div", class_="s-main-slot s-result-list s-search-results sg-row")

print(atag.text)
#print(result.contents)

#driver.close();