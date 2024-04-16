
import requests
from twilio.rest import Client
account_sid = "AC2c1f8341377b4e0905d0563ea9441f87"
auth_token = "99126ce7de79bcccdaf24c17215bf130"


STOCK_NAME = "TSLA"


STOCK_API_KEY = "HFS3RJ49YWBYTH44"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"



parameters = {
"function":"TIME_SERIES_DAILY",
"symbol":"TSLA",
"apikey":"HFS3RJ49YWBYTH44"
}


response = requests.get(STOCK_ENDPOINT,parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
stocks_prices_list = [value for (key,value) in data.items()]
yesterday_price = float(stocks_prices_list[0]["4. close"])
today_price = float(stocks_prices_list[1]["4. close"])
gain_lose = today_price - yesterday_price
rate = (gain_lose * 100) / yesterday_price
print(yesterday_price)
print(today_price)
print(gain_lose)
print(f"{rate}%")


NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Tesla Inc"



new_parameters = {
    "apiKey":"85e3d0dd5d8d49f78aefdb7da07a1836",
    "qInTitle":COMPANY_NAME,  
   
}

up_down = None

if gain_lose > 0:
    up_down = "⬆️" 
else:
    up_down = "⬇️" 

if abs(gain_lose) > 1:
    new_response = requests.get(NEWS_ENDPOINT,new_parameters)
    new_response.raise_for_status()
    data_new = new_response.json()["articles"]
    three_articles = data_new[0:3]


    # "{Headlines: {article title}. \n Brief: {article description}}"
    formated_articles = [f"{STOCK_NAME}:{up_down} {rate}% Headlines: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    client = Client(account_sid, auth_token)
    for message in three_articles:
        client.messages.create(
                                body=message,
                                from_="+19292961782",
                                to="+41774811118"
                            )
        print(message.status)

























    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

