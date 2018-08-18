# Acquia-Partner-Scraper
2 scripts that will scrape acquia.com for their partner data.

Acquia_Partner_Link_Scraper.py will grab all of the partner overview links from Acquia's partner finder at https://www.acquia.com/partners/finder, and save all of the links to a text file called Partner_List.txt for further scraping.

Acquia_Partner_Page_Scraper.py will scrape all of the partner links from the Partner_List created by Acquia_Partner_Link_Scraper.py. It will save each partner's Domain Name, Comany Name, Country Location and Website Status code into a csv file named Acquia_Partner_Info.csv.

I am using time.sleep(1) at the end of each request loop so the site won't block my IP.
