import requests
from bs4 import BeautifulSoup


def parse_habr_news():
    url = "https://habr.com/ru/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news = []
    for article in soup.find_all('article', class_='tm-articles-list__item'):
        title = article.find('a', class_='tm-title__link').text.strip()
        link = "https://habr.com" + article.find('a', class_='tm-title__link')['href']
        news.append({"title": title, "link": link})

    return news


# Пример вызова
if __name__ == "__main__":
    news = parse_habr_news()
    for item in news[:10]:  # Вывод первых 10 новостей
        print(f"{item['title']} - {item['link']}")