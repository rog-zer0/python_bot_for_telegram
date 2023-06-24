import telebot
import extensions

# Укажите токен вашего бота, который вы получили от BotFather
TOKEN = '6168323437:AAE-A141p_jPrwJcOcA8gkIpXCKce_7VdU0'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_instructions(message):
    instructions = "Привет! Я бот для конвертации валют.\n\n" \
                   "Мой криворукий создатель написал меня для теста.\n" \
                   "Было очень интересно, но нихрена не понятно...\n" \
                   "Чтобы получить бесполезную инфу о ценах на валюту, отправьте сообщение в формате:\n" \
                   "<имя валюты, цену которой вы хотите узнать> " \
                   "<имя валюты, в которой надо узнать цену первой валюты> " \
                   "<количество первой валюты>\n\n" \
                   "Например:\n" \
                   "USD EUR 100\n\n" \
                   "Для получения списка доступных валют введите команду /values"
    bot.reply_to(message, instructions)


@bot.message_handler(commands=['values'])
def send_currency_values(message):
    currency_values = "Доступные валюты:\n" \
                      "USD - Доллар США\n" \
                      "EUR - Евро\n" \
                      "RUB - Российский рубль"
    bot.reply_to(message, currency_values)


@bot.message_handler(func=lambda message: True)
def convert_currency(message):
    try:
        input_data = message.text.split()
        if len(input_data) != 3:
            raise extensions.APIException("Неправильный формат запроса")

        base_currency, quote_currency, amount = input_data

        price = extensions.CurrencyConverter.get_price(base_currency, quote_currency, amount)
        result = f"Цена {amount} {base_currency} в {quote_currency} = {price}"
        bot.reply_to(message, result)
    except extensions.APIException as e:
        bot.reply_to(message, f"Ошибка: {e.message}")


# Запуск бота
bot.polling()