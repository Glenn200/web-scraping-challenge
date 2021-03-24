# Dependencies
import pandas as pd
#import splinter
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize browser
def init_browser(): 
    # Replace the path with your actual path to the chromedriver
    exec_path = {'executable_path': '/app/.chromedriver/bin/chromedriver'}
    return Browser('chrome', headless=True, **exec_path)

# Create Mission to Mars dictionary that can be imported into Mongo
mars_info = {}

# NASA MARS NEWS

def scrape():
   
    try:
        
        # Initialize browser 
        browser = init_browser()
        
        # Visit Mars NASA News Site
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        # Optional delay for loading the page
        browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
        html = browser.html
        news_soup = bs(html, 'html.parser')
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        
        # Get the latest news title
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
        #news_p

        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_p
        
        return mars_info
    
    finally:
        
        browser.quit()

    # FEATURED IMAGE
    # JPL Mars Space Images

        try:
        
            # Initialize browser 
            browser = init_browser()
        
        
        
        
        
        finally:
        
            browser.quit()