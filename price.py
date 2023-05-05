import requests
from bs4 import BeautifulSoup
import cloudscraper
import pandas as pd
import time
import datetime

scraper = cloudscraper.create_scraper()  

def scrape_price(try_time = 0):

    if try_time == 10:
        return
    
    url_to_scrape = "https://www.investing.com/commodities/aluminum"

    print(f"Scraping try_time::{try_time} {url_to_scrape} {datetime.datetime.now()}.")
    
    req = scraper.get(url_to_scrape).text
    # mask = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',

    page_soup = BeautifulSoup(req, 'html.parser')

    # print(page_soup)
    try:
        price = page_soup.find('div',class_ = "text-5xl").text
        print(price)
        df = pd.DataFrame({"Aluminum Price":['live aluminum price pulled from investing.com'],"":[price]}).to_excel("Commlive.xlsx",index = False)
    except:
        time.sleep(5)
        scrape_price(try_time = try_time + 1)


    
 
    
if __name__ == '__main__':

    while True:

        scrape_price()

        time.sleep(900)
    



