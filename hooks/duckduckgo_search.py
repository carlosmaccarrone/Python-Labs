import requests
from bs4 import BeautifulSoup

def duckduckgo_search(query):
    """
    Perform a search query on DuckDuckGo and return a list of result URLs.

    Args:
        query (str): The search query string.

    Returns:
        list of str: URLs of search results from DuckDuckGo.

    Note:
        This function scrapes the HTML results page from DuckDuckGo's
        lightweight HTML version. The structure of the page may change,
        which can break the scraper.

    Raises:
        requests.HTTPError: If the HTTP request to DuckDuckGo fails.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://html.duckduckgo.com/html/?q={query.replace(" ", "+")}'

    response = requests.post(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    # DuckDuckGo results links are inside 'a' tags with class 'result__a'
    for a in soup.find_all('a', class_='result__a'):
        href = a.get('href')
        if href:
            results.append(href)
    return results

if __name__ == '__main__':
    query = input("Enter your search query: ")
    links = duckduckgo_search(query)
    print("\nDuckDuckGo search results:\n")
    for link in links:
        print(link)
        
# pip install requests beautifulsoup4