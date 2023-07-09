import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    #Send a GET request to the initial URL
    response = requests.get(url)
    
    #Check if the request was successful
    if response.status_code == 200:
        #Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        #Extract data from the current page
        data = extract_data(soup)
        
        #Check if there are additional pages
        next_page_link = soup.find('a', class_='next-page-link')
        if next_page_link:
            #Recursively call the web_scraper function for the next page
            next_page_url = url + next_page_link['href']
            data += web_scraper(next_page_url)
        
        #Return the scraped data
        return data
    else:
        #Print an error message if the request was unsuccessful
        print('Error:', response.status_code)

def extract_data(soup):
    #Extract specific data from the HTML, in this case only looking for h2 elements with class title, but could search for anything
    data = []
    titles = soup.find_all('h2', class_='title')
    for title in titles:
        data.append(title.text.strip())
    
    return data

#Example usage
url = 'https://example.com/page-1'
scraped_data = web_scraper(url)
if scraped_data:
    print('Scraped Data:')
    for item in scraped_data:
        print(item)
else:
    print('Web scraping failed.')