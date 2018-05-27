#importing libraries

import requests
from bs4 import BeautifulSoup

# Website to extract review information from: HardcoreGamer

# Review of Need for Speed: Payback
url = 'https://www.hardcoregamer.com/2017/11/06/review-need-for-speed-payback/278450/'
response = requests.get(url)
html = response.content

# Parsing the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
review = []
for i in range(12):
    review.append(soup.find_all('p')[i].get_text())
