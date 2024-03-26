# Импорт необходимых модулей
from tok import key, apiKey
from aiogram import Bot, Dispatcher, executor, types # Импорт классов и функций из библиотеки aiogram
import requests
import json

# Создание экземпляра бота и диспетчера
bot = Bot(token=key)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Получить Прогноз погоды", callback_data="city"))
    markup.add(types.InlineKeyboardButton("Список команд", callback_data="list"))
    await message.reply("Привет, здесь вы можете получить прогноз погоды", reply_markup=markup)

# Обработчик команды /listCity
@dp.message_handler(commands=['listCity'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Казань'))
    markup.add(types.KeyboardButton('Йошкар-Ола'))
    await message.reply("Привет", reply_markup=markup)

# Обработчик коллбэков
@dp.callback_query_handler()
async def callback(call):
    if call.data == 'list':
        await call.message.answer('/listCity\n/start')
    elif call.data == 'city':
        await call.message.answer('Введите город')

# Обработчик текстовых сообщений
@dp.message_handler(content_types=['text'])
async def reply(message: types.Message):
    city = message.text.lower().strip()
    url = f"OpenWeather"
    res = requests.get(url)
    data = json.loads(res.text)
    if res.status_code == 200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        desc = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        listEmoji = ["🌡", "💦", "🌬", "💨"]
        await message.reply(f"Погода в городе {message.text}\n"
                            f"Температура {temp} C {listEmoji[0]}\n"
                            f"Влажность {humidity}% {listEmoji[1]}\n"
                            f"Давление {pressure} Pa {listEmoji[2]}\n"
                            f"Скорость ветра {wind_speed} м/с {listEmoji[3]}\n"
                            f"Описание {desc}")
    elif res.status_code == 404:
        await message.reply(f"Город не найден")

# Запуск бота
executor.start_polling(dp)
