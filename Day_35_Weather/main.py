import requests

# So, my cell phone plan is weird and doesn't play well with SMS, so I wasn't able to use Twilio like the teacher asked.
# I used a Telegram bot instead, per the recommendation of Rustaf in the comments and following the instructions in the
# following article:
# https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e


def telegram_bot_sendtext():
    bot_token = "tokengoeshere"
    bot_chatID = "blahblahblah"
    send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage" \
                f"?chat_id={bot_chatID}" \
                f"&parse_mode=Markdown&text='It's going to rain. Bring an umbrella!'"
    txt_response = requests.get(send_text)
    return txt_response.json()


parameters = {
    "lat": 0,
    "lon": 0,
    "units": "imperial",
    "exclude": "currently,minutely,daily",
    "appid": "noneyo"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for f in weather_slice:
    if weather_data["hourly"][0]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    telegram_bot_sendtext()
