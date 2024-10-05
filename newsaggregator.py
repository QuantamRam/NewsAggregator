import requests
import argparse

API_KEY = 'ef394a9b79524ad98733f3f5662a6df5'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

def get_news(category=None, country='us'):
    """
    Function to fetch news from NewsAPI.
    
    :param category: Optional category to filter news.
    :param country: Country code to fetch news from a specific location.
    :return: List of news articles.
    """
    params = {
        'apiKey': API_KEY,
        'country': country,
        'category': category,
        'pageSize': 10,  # Number of articles to return
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        news_data = response.json()
        return news_data.get('articles', [])
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def display_news(articles):
    """
    Function to display news articles in a clean format.
    
    :param articles: List of articles.
    """
    if not articles:
        print("No articles found!")
        return
    
    for idx, article in enumerate(articles):
        print(f"{idx + 1}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   URL: {article['url']}")
        print("")
if __name__ == '__main__':
   
    parser = argparse.ArgumentParser(description="Personalized News Aggregator")
    parser.add_argument('--category', type=str, help="News category (e.g., technology, sports, health)")
    parser.add_argument('--country', type=str, default='us', help="Country code (e.g., us, in, uk)")
    args = parser.parse_args()
    news_articles = get_news(category=args.category, country=args.country)
    display_news(news_articles)
