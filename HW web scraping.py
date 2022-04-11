import requests
import bs4

url_ru = 'https://habr.com/ru'
url = 'https://habr.com'
HEADERS = ''

KEYWORDS = ['Python *', 'JavaScript *', 'Изучение языков', 'IT-компании']

response = requests.get(url_ru, headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    for hub in hubs:
        if hub in KEYWORDS:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            date = article.find('span', class_='tm-article-snippet__datetime-published').find('time').attrs['title']
            url_ = url + href
            title = article.find('h2').find('span').text
            result = f'Статья {title} - {url_} - {date}'
            print(result)