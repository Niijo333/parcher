
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Union

def parse_news(url: str, tag: str = 'h3') -> List[Dict[str, Union[str, None]]]:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching the URL {url}: {e}")
        return []

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all(tag)
    except Exception as e:
        print(f"Error while parsing the HTML: {e}")
        return []

    news_data = []
    for headline in headlines:
        news = {
            'title': headline.text.strip(),
            'link': None,
            'description': None,
            'date': None
        }

        # Extract link
        parent = headline.find_parent('a')
        if parent and parent.has_attr('href'):
            news['link'] = parent['href']

        # Extract description and date
        # This part will depend on the website structure and may require customization
        # For the BBC News example, we'll skip this part

        news_data.append(news)
    
    return news_data

# Example usage
if __name__ == '__main__':
    url = 'https://www.bbc.com/news'
    news_data = parse_news(url)
    print(news_data[:5]) # Display the first 5 news items
