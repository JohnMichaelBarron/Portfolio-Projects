#Main_GUI_Scraper_Module.py 

from HackerNewsScraper import scrape_hacker_news
from GuiScraper import load_headlines, create_gui 

#file path the save and read data
file_path = r"D:\Python\vsCode python projects\Portfolio_Projects\hacker_news_headlines.csv"


#scrape and save the data
scrape_hacker_news(file_path)

#load data and display GUI
headlines = load_headlines(file_path)
if headlines: 
    create_gui(headlines)
else:
    print("No headlines to display.")

    