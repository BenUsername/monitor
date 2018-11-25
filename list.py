import os
os.system('cls' if os.name == 'nt' else 'clear') # clear terminal for both windows and Unix

import requests
from bs4 import BeautifulSoup

#make loop to browse all pages until error.

# set the url as VentureBeat

list = []

while names != []:

    for k in range(1,50+1):

    names = "start"

        url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&SIC=2836&owner=include&match=&start={k*100}&count=100&hidefilings=0"
        # set the headers like we are a browser,
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        # download the homepage
        response = requests.get(url, headers=headers)
        # parse the downloaded homepage and grab all text, then,
        soup = BeautifulSoup(response.text, "lxml")
        names  = soup.findAll("tr")
        list += names

print(list)
