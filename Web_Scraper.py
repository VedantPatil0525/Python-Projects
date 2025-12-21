# 📌 Goal:  
# Scrape titles of articles from a blog or news website (e.g., https://quotes.toscrape.com)

import requests
from bs4 import BeautifulSoup

base_url = 'https://quotes.toscrape.com'
current_url = base_url

while current_url:
  response = requests.get(current_url)
  soup = BeautifulSoup(response.text, 'html.parser')

  quotes = soup.find_all('span', class_='text')

  for quote in quotes:
    print("-", quote.text)

  next_button = soup.find_all('li', class_='next')

  if next_button:
    next_page = next_button[0].find('a')['href']
    current_url = base_url + next_page
  else:
    current_url = None