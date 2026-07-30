from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze(news, stocks):

    prompt = f"""
오늘 뉴스

{news}

현재 주가

{stocks}

너는 대한민국 최고의 주식 애널리스트다.

다음을 알려줘.

1. 오늘 시장 분위기
2. 보유종목 영향
3. 추가매수 추천
4. 주의해야 할 종목
5. 5줄 요약

한국어로 답변.
"""

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return response.output_text