import csv
import requests
from bs4 import BeautifulSoup
import time

# Open our list of links from the partner finder
links = open('/home/cdog/Desktop/Acquia-Partner-Scraper/Partner_List(copy).txt', 'r')

# open csv file to store partner info
with open('/home/cdog/Desktop/Acquia-Partner-Scraper/Acquia_Partner_Info-TAKE2(copy).csv', 'w') as csvfile:
    ## Set field names of data
    fieldnames = ['Domain_Name', 'Company_Name', 'Country/Countries', 'Site_Status_Code']
    # Start csv writer
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # Write the field names
    writer.writeheader()
    
    ## Loop through links
    for i in links:
        # Make request to Partner page
        try:
            r = requests.get(i.strip())
        # Log error if we have a bad link
        except requests.exceptions.RequestException as e:
            fail = open('/home/cdog/Desktop/Acquia-Partner-Scraper/log.txt', 'a') 
            fail.write(str(e))
            fail.close()            
            
        # Make html into soup
        soup = BeautifulSoup(r.text, "html.parser")
    
        # Grab Partner name
        Partner_Name = soup.find("h1", {"id": "page-title"}).text.encode("utf-8")
    
        ## Grab the 'fieldset' tag - tag contains the rest of the partner info.
        fieldset_tag = soup.find('fieldset')
    
        ##  Get Partner URL
        theAtag = fieldset_tag.find('a')
        try:
            Partner_URL = theAtag.get('href')
        except:
            Partner_URL = 'NO LINK'
            
        ## Get Country names
        country_tag = fieldset_tag.find_all("div", {"class": "country-name"})
        ## Some partners are in multiple countries.
        Partner_Countries = []
        if len(country_tag) >= 1:
            for i in country_tag:
                Partner_Countries.append(i.text.strip().encode("utf-8"))
        else:
            try:
                Partner_Countries.append(unicode(country_tag[0].text.strip()))
            except:
                Partner_Countries.append('N/A')
            
        ## check partner site's status code
        try:
            Status_Code = requests.get(Partner_URL).status_code
        except requests.exceptions.RequestException as e:
            Status_Code = e
        
        ## Write data to csv file
        writer.writerow({'Domain_Name': Partner_URL, 'Company_Name': Partner_Name.strip(), 'Country/Countries': unicode(str(Partner_Countries)), 'Site_Status_Code': str(Status_Code)[-77:]})
            
        # Wait a sec so we dont get our IP blocked
        time.sleep(1)

print('Done Writing!')

