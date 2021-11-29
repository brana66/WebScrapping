#scapping data from indeed.com

import requests
from bs4 import BeautifulSoup
import sys

#print()
print("--------------Sending request--------------")
url = "https://in.indeed.com/jobs?q=full%20stack%20developer&l=Mumbai"
page = requests.get(url)
#print(page.text)

#print()
print("--------------parsing html--------------")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

#print()
print("--------------Fetching data--------------")
result = soup.find(id="mosaic-provider-jobcards")
jobs = result.findAll('td', class_='resultContent')
#print(result)

for job in jobs:
    #title_element = job.find("h2", class_="jobTitle jobTitle-color-purple")
    title_element = job.findAll("span")[1]
    company_element = job.find("span", class_="companyName")
    location_element = job.find("div", class_="companyLocation")

    sys.stdout = open("indeed_search.txt", "a")

    if title_element == company_element:
       title_element = job.findAll("span")[0]
       print(title_element.text.strip())
    else:
        title_element = job.findAll("span")[1]
        print(title_element.text.strip())

    print(company_element.text.strip())
    print(location_element.text.strip())

    print()

print("Listed jobs: " + str(len(jobs)))
sys.stdout.close()