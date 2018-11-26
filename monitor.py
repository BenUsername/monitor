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

list_recent = []
text = "start"

for k in range (0,5+1):
    # set the url as VentureBeat,
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

with open("list_recent.html", "w") as file:
    file.write(str(list_recent))

list_names = []
names = "start"

for k in range(0,10+1):

    url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&SIC=2836&owner=include&match=&start={k*100}&count=100&hidefilings=0"
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

with open("list_names.html", "w") as file:
    file.write(str(list_names))


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
        server.login("maxbaude0@gmail.com", "professeur7")

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
