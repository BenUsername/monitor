# In this script we scrap two websites, one with a list of companies, one with recent news, and check whether any news applies to our 
# list of company. If that is the case, we send an email indicating that fact. 

import os
os.system('cls' if os.name == 'nt' else 'clear') # clears terminal for both windows and Unix

# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# *** SCRAP LIST OF NEWS *** 

list_recent = []
text = "start"

for k in range (0,5+1):
    # set the url 
    url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=&SIC=&State=&Country=&CIK=&owner=only&accno=&start={k*100}&count=100"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    text = [td.text for td in soup.find_all('a')]

    if text == []:
        break

    else:
        list_recent += text

        
# saves the list of news as html so that we can potentially work on it without re-scraping, reducing risk of ban from websites        
with open("list_recent.html", "w") as file:
    file.write(str(list_recent))

# *** SCRAP LIST OF COMPANIES ***    
    
list_names = []
names = "start"

for k in range(0,10+1):

    url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&SIC=2834&owner=include&match=&start={k*100}&count=100&hidefilings=0"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    html = response.text
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(html, "lxml")

    names = [td.text for td in soup.find_all('td')]

    if names == []:
        break

    else:
        list_names += names

# saves the list of news as html so that we can potentially work on it without re-scraping, reducing risk of ban from websites   
        
with open("list_names.html", "w") as file:
    file.write(str(list_names))

# *** MATCH & EMAIL *** 
# checks if list of news mentions one of the companies and send an email if that is the case

for company in list_recent:
    if company in list_names:
        
        print(f"{company} has recent news")

        # create an email message with just a subject line,
        msg = f'Subject: This is Ben\'s script talking, {company} has recent news'
        # set the 'from' address,
        fromaddr = 'maxbaude0@gmail.com'
        # set the 'to' addresses,
        toaddrs  = ['btann93@gmail.com','ben.tannenbaum1@gmail.com', 'b.tannenbaum88@gmail.com']

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("maxbaude0@gmail.com", ********) #replace with email p/word when using script

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        #send the email
        server.sendmail(fromaddr, toaddrs, msg)
        #disconnect from the server
        server.quit()

    else:
        continue
