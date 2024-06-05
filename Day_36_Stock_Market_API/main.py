import requests
import vonage

API_KEY_FOR_STOCK = "V7Q9K6BXJ55W6320"
API_KEY_FOR_NEWS = "96a5e8307faa4ff98b16c698cacfadc5"


def get_stock_data():
    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": "TATAELXSI.BSE",
        "apikey": API_KEY_FOR_STOCK,
    }
    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = dict(list(response.json()["Time Series (Daily)"].items())[:2])

    data = [float(info['4. close']) for (date, info) in data.items()]
    return data


def analyse(data: list) ->str:
    if data[0] > data[1]:
        difference = data[0] - data[1]
        percentage = (difference / data[0]) * 100
        return f"Tata ELXSI: ↑{'%.2f'% percentage}%"

    else:
        difference = data[1] - data[0]
        percentage = (difference / data[0]) * 100
        return f"Tata ELXSI: ↓{'%.2f'% percentage}%"


def get_news():
    parameters = {
        "apiKey" : API_KEY_FOR_NEWS,
        "category" : "business",
        "q" : "ELXSI",
        "pageSize" : 1,
        "country" : "in",
    }
    response = requests.get(url="https://newsapi.org/v2/top-headlines", params=parameters)
    response.raise_for_status()
    try:
        heading = response.json()['articles'][0]['title']
        body = response.json()['articles'][0]['description']
    except IndexError:
        return "No News for Today"
    else:
        return f"HEADING: {heading}\nBRIEF: {body}"


def send_msg(msg):
    client = vonage.Client(key="611f9916", secret="B4ZIKC9dqZVGEktw")
    sms = vonage.Sms(client)
    status = sms.send_message(
        {
            "from" : "918910284642",
            "to" : "918910284642",
            "text" : msg,
        }
    )

    if status["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {status['messages'][0]['error-text']}")


data = get_stock_data()
report = analyse(data)
news = get_news()

final_msg = f"{report}\n{news}"
send_msg(final_msg)
