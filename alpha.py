import requests
import telebot

API_KEY = "1949608059:AAGlFyBdr8FW1d9U7kQB-_HFxk8ncAA3_xs"
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["start", "hi", "hello", "heythere", "hey"])
def Hi(message):
    bot.send_message(message.chat.id, f"Hi {message.from_user.first_name}!")


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Hi I'm Sara.I'm a weather bot.I can provide the weather informations of the city you want",
    )


@bot.message_handler(commands=["urname", "yourname"])
def sara(message):
    bot.send_message(message.chat.id, "I'm Sara")


@bot.message_handler(func=lambda message: True)
def weather(message):
    try:
        cid = message.chat.id
        mid = message.message_id
        message_text = message.text
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        weather_link = f"http://api.openweathermap.org/data/2.5/weather?appid=8e5d5c219dd7b7df4db4f188d6f99cb0&q={message_text}"
        data = requests.get(weather_link).json()
        one = data.get("coord")
        weather = data["weather"]

        for i in weather:
            main = i.get("main")
            description = i.get("main")

        main = data.get("main")
        min = main.get("temp_min")
        max = main.get("temp_max")
        pressure = main.get("pressure")
        humidity = main.get("humidity")

        name = data.get("name")

        sys = data.get("sys")
        country = sys.get("country")

        weather_data = f"min_temp:{min} \n max_temp:{max} \n description:{description} \n pressure:{pressure} \n humidity:{humidity} \n name:{name} \n country:{country}"

        bot.send_message(message.chat.id, weather_data)
    except KeyError:
        bot.send_message(message.chat.id, "Sorry i can't understand what you said.")


bot.polling()
