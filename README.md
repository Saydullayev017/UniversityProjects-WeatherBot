
### Бот погоды на Python с использованием библиотеки aiogram

Этот бот погоды на Python использует библиотеку aiogram для обработки сообщений и запросов пользователей. Бот позволяет получать прогноз погоды для указанного города с использованием API OpenWeatherMap.

### Инструкции по запуску:

1. Установите необходимые библиотеки, выполнив команду:
   ```
   pip install aiogram requests
   ```

2. Получите API ключи для OpenWeatherMap и Telegram Bot API.

3. Создайте файл `tok.py` и определите в нем переменные `key` (API ключ Telegram Bot) и `apiKey` (API ключ OpenWeatherMap).

4. Запустите бот, выполнив команду:
   ```
   python main.py
   ```

### Как использовать бота:

1. Напишите `/start`, чтобы начать общение с ботом.
2. Выберите "Получить Прогноз погоды" для запроса погоды или "Список команд" для просмотра доступных команд.
3. Введите название города для получения прогноза погоды.
4. Бот отправит информацию о погоде в выбранном городе.

### Структура проекта:

- `main.py`: Основной файл с кодом бота.
- `tok.py`: Файл с API ключами.


### Дополнительная информация:

- Для работы бота необходимо наличие интернет-соединения.
- Бот использует данные о погоде с сайта OpenWeatherMap, поэтому убедитесь в корректности API ключа OpenWeatherMap.
- При возникновении проблем обратитесь к документации aiogram и OpenWeatherMap для получения дополнительной информации.

### Автор:

Saydullayev017


---

Этот README поможет пользователям понять, как запустить и использовать вашего бота погоды на Python с библиотекой aiogram.