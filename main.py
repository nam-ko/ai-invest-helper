from news import get_news
from stocks import get_stock_data
from ai import analyze

print("=" * 50)
print("🤖 AI 투자비서")
print("=" * 50)

print("\n📰 뉴스 가져오는 중...")

news = get_news()

for n in news:
    print("-", n)

print("\n📈 주가 가져오는 중...")

stocks = get_stock_data()

for s in stocks:
    print(
        f"{s['name']} ({s['ticker']}) "
        f"{s['price']}원 "
        f"{s['shares']}주"
    )

print("\n🤖 AI 분석 중...")

result = analyze(news, stocks)

print("\n")
print("=" * 50)
print(result)
print("=" * 50)