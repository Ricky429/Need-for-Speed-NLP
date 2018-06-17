#importing libraries

import requests
from bs4 import BeautifulSoup

# Websites to extract review information from: HardcoreGamer

urls = ['https://www.hardcoregamer.com/2017/11/06/review-need-for-speed-payback/278450/', 
        'https://www.hardcoregamer.com/2007/11/13/review-need-for-speed-prostreet/30732/',
        'https://www.hardcoregamer.com/2013/11/16/review-need-for-speed-rivals-ps4/62652/',
        'https://www.hardcoregamer.com/2015/11/02/review-need-for-speed/175167/',
        'https://www.hardcoregamer.com/2012/10/30/review-need-for-speed-most-wanted/16930/']
    
# Review of Need for Speed: Payback
url_payback = urls[0]
response_payback = requests.get(url_payback)
html_payback = response_payback.content

# Review of Need for Speed: ProStreet
url_prostreet = urls[1]
response_prostreet = requests.get(url_prostreet)
html_prostreet = response_prostreet.content

# Review of Need for Speed: Rivals
url_rivals = urls[2]
response_rivals = requests.get(url_rivals)
html_rivals = response_rivals.content

# Review of Need for Speed
url_reboot = urls[3]
response_reboot = requests.get(url_reboot)
html_reboot = response_reboot.content

# Review of Need for Speed: Most Wanted
url_mostwanted = urls[4]
response_mostwanted = requests.get(url_mostwanted)
html_mostwanted = response_mostwanted.content

# Parsing the HTML using BeautifulSoup
soup_payback = BeautifulSoup(html_payback, 'html.parser')
review_payback = []
for i in range(12):
    review_payback.append(soup_payback.find_all('p')[i].get_text())
    
soup_prostreet = BeautifulSoup(html_prostreet, 'html.parser')
review_prostreet = []
for i in range(11):
    review_prostreet.append(soup_prostreet.find_all('p')[i].get_text())
    
soup_rivals = BeautifulSoup(html_rivals, 'html.parser')
review_rivals = []
for i in range(12):
    review_rivals.append(soup_rivals.find_all('p')[i].get_text())
    
soup_reboot = BeautifulSoup(html_reboot, 'html.parser')
review_reboot = []
for i in range(12):
    review_reboot.append(soup_reboot.find_all('p')[i].get_text())
    
soup_mostwanted = BeautifulSoup(html_mostwanted, 'html.parser')
review_mostwanted = []
for i in range(12):
    review_mostwanted.append(soup_mostwanted.find_all('p')[i].get_text())

#Creating the DataFrames
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Most Wanted Review
mostwanted_review = pd.DataFrame({'Review' : review_mostwanted})
mostwanted_year = []
for row_mostwanted in mostwanted_review['Review']:
    if not row_mostwanted:
        mostwanted_year.append("")
    else:
        mostwanted_year.append("2012")
        
mostwanted_review['Year'] = mostwanted_year
mostwanted_review.drop(mostwanted_review.index[[0, 3, 6, 9]], inplace=True)

# Pro Street Review
prostreet_review = pd.DataFrame({'Review' : review_prostreet})
prostreet_year = []
for row_prostreet in prostreet_review['Review']:
    if not row_prostreet:
        prostreet_year.append("")
    else:
        prostreet_year.append("2007")
        
prostreet_review['Year'] = prostreet_year
prostreet_review.drop(prostreet_review.index[[0, 3, 7]], inplace=True)

# Payback Review
payback_review = pd.DataFrame({'Review' : review_payback})
payback_year = []
for row_payback in payback_review['Review']:
    if not row_payback:
        payback_year.append("")
    else:
        payback_year.append("2017")
        
payback_review['Year'] = payback_year
payback_review.drop(payback_review.index[[0]], inplace=True)

# Rivals Review
rivals_review = pd.DataFrame({'Review' : review_rivals})
rivals_year = []
for row_rivals in rivals_review['Review']:
    if not row_rivals:
        rivals_year.append("")
    else:
        rivals_year.append("2013")
        
rivals_review['Year'] = rivals_year
rivals_review.drop(rivals_review.index[[0, 4, 7, 10]], inplace=True)

# Reboot Review
reboot_review = pd.DataFrame({'Review' : review_reboot})
reboot_year = []
for row_reboot in reboot_review['Review']:
    if not row_reboot:
        reboot_year.append("")
    else:
        reboot_year.append("2015")
        
reboot_review['Year'] = reboot_year
reboot_review.drop(reboot_review.index[[0]], inplace=True)

# Combnining the review DataFrames
reviews = mostwanted_review.append(payback_review, ignore_index=True)
reviews = reviews.append(prostreet_review, ignore_index=True)
reviews = reviews.append(reboot_review, ignore_index=True)
reviews = reviews.append(rivals_review, ignore_index=True)
















