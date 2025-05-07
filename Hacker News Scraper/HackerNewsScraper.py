#HackerNewsScraper.py
def scrape_hacker_news(file_path):

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import csv 

    driver = webdriver.Chrome()  # ChromeDriver will now work
    driver.get("https://news.ycombinator.com/")

    headlines = driver.find_elements(By.CLASS_NAME, "titleline")
    data = []


    for index, headline in enumerate(headlines):
        text = headline.text
        try: 
            url = headline.find_element(By.TAG_NAME, "a").get_attribute("href")
        except Exception:
            url = "No URL Found"
        data.append((index + 1, text, url))
        
    driver.quit()


    #open a file to save the headlines 
    file_path = r"D:\Python\vsCode python projects\Portfolio_Projects\hacker_news_headlines.csv"

    with open(file_path, "w", newline ="", encoding = "utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "Headline", "URL"])  #writes the header row
        writer.writerows(data)

        


    
