import os
os.system('cls' if os.name == 'nt' else 'clear') # clears terminal for both windows and Unix

#checks if a given company name is in an html file

from bs4 import BeautifulSoup
import re

#company name:
company = "ABGENIX"

#html file:
html = "list_company.html"

with open(html, "r") as file:

        #parses html
        soup = BeautifulSoup(file, "lxml")
        #extract text
        list = [td.text for td in soup.find_all('td')]
        #checks if company name is in text 
        if any(company in s for s in list):
            print("oh yeah baby")
        else:
            print("...")
