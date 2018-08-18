import requests
from bs4 import BeautifulSoup
import time

#  Acquia's pages range from 0 to 40 #
baseurl='https://www.acquia.com/partners/finder?page='

# Creating list because some partners have multiple links and we only want one.
partner_urls=[]

# Loop through a range - Currently there are only 40 pages of partners
for finderpage in range(0, 41):
    # Make request to Partner Finder page
    r = requests.get(baseurl+str(finderpage))
    # Make html into soup
    soup = BeautifulSoup(r.text, "html.parser")  # r.text
    # Loop through all 'a' tags on page
    for link in soup.find_all('a'):
        # Check if link matches the base link of a partner page
        if '/partners/showcase/' in str(link.get('href')):
            # Check if link is already in our partner list
            if str(link.get('href')) in partner_urls:
                pass
            else:
                # Append link to partner list
                partner_urls.append(str(link.get('href')))
    # Slow down the number of requests in case they block IP            
    time.sleep(1)

# Open file to store links to partners
x = open("/home/cdog/Desktop/Acquia-Partner-Scraper/Partner_List.txt", "w")
# Loop through list and write each URL to file
for i in partner_urls:
    x.write('https://www.acquia.com'+i+'\n')
# Close the file!
x.close()



