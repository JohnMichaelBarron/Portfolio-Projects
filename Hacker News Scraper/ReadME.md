# Hacker News GUI Scraper

A Python application that scrapes the latest headlines from [Hacker News](https://news.ycombinator.com/), stores them in a CSV file, and displays them in a scrollable GUI. Each headline is clickable and opens the associated link in the default web browser.

## Features

- **Automated Web Scraping**: Extracts headlines and URLs from the Hacker News homepage using Selenium.
- **CSV Export**: Saves headlines to a local `.csv` file with headline text and link.
- **Graphical User Interface**: Displays headlines in a `tkinter`-based GUI with a scrollable layout.
- **Interactive Links**: Each headline is clickable and opens the article in the browser.

## Project Structure
├── GuiScraper.py # GUI to load and display headlines from CSV
├── HackerNewsScraper.py # Scraper using Selenium to collect headlines
├── Main_GUI_Scraper_Module.py # Main runner to scrape data and launch GUI
├── hacker_news_headlines.csv # Output file created by scraper



## Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed and accessible via system PATH

### Python Packages

Install required packages with:

```bash
pip install selenium


git clone https://github.com/your-username/hacker-news-gui-scraper.git
cd hacker-news-gui-scraper

### Usage 
python Main_GUI_Scraper_Module.py