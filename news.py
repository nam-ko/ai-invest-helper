import requests
from config import NEWS_API_KEY

def get_news():
    url = (
        f"https://newsapi.org/v2/top-headlines"
        f"?category=business&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("status") != "ok":
            return ["뉴스를 가져오지 못했습니다."]

        return [article["title"] for article in data["articles"]]

    except Exception as e:
        return [f"오류: {e}"]