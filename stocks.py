import json
import yfinance as yf

def get_stock_data():
    with open("portfolio.json", "r", encoding="utf-8") as f:
        portfolio = json.load(f)

    result = []

    for stock in portfolio["stocks"]:
        try:
            ticker = yf.Ticker(stock["ticker"])
            info = ticker.fast_info

            result.append({
                "name": stock["name"],
                "ticker": stock["ticker"],
                "shares": stock["shares"],
                "price": info.get("lastPrice", 0)
            })

        except Exception:
            result.append({
                "name": stock["name"],
                "ticker": stock["ticker"],
                "shares": stock["shares"],
                "price": "조회 실패"
            })

    return result