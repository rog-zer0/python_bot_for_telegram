import requests
import json


class APIException(Exception):
    def __init__(self, message):
        self.message = message


class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base = base.upper()
            quote = quote.upper()
            amount = float(amount)

            if base == quote:
                raise APIException("Вы ввели одинаковые валюты")

            url = f"https://api.exchangerate-api.com/v4/latest/{base}"
            response = requests.get(url)
            data = json.loads(response.text)

            if quote not in data['rates']:
                raise APIException("Неправильно введено имя валюты")

            exchange_rate = data['rates'][quote]
            result = exchange_rate * amount

            return result
        except ValueError:
            raise APIException("Неправильно введено число")
        except requests.exceptions.RequestException:
            raise APIException("Ошибка при подключении к API")


# Используйте этот метод для получения цены на валюту в боте
# price = CurrencyConverter.get_price('USD', 'EUR', 100)