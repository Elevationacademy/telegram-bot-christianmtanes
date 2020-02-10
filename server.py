from flask import Flask, Response, request
import requests

from math_ops import *
TOKEN = '1040316148:AAE_-EBgE_FytQxGzhiw8YTw1anKkE9T17k'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://ca56c996.ngrok.io/message'.format(TOKEN)

app = Flask(__name__)


@app.route('/sanity')
def sanity():
    return "Server is running"

@app.route('/message', methods=["POST"])
def check_message():
    print("got message")
    chat_id = request.get_json()['message']['chat']['id']
    text = request.get_json()['message']['text']
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                       .format(TOKEN, chat_id, "Got it"))

    is_prime_message = "is prime = {}".format(is_prime(text))
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                 .format(TOKEN, chat_id, is_prime_message))

    factorial_message = "factorial = {}".format(factorial(text))
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                 .format(TOKEN, chat_id, factorial_message))

    palindrome_message = "is palindrome = {}".format(is_palindrome(text))
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                 .format(TOKEN, chat_id, palindrome_message))

    sqrt_message = "is sqrt integer = {}".format(is_sqrt(text))
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                 .format(TOKEN, chat_id, sqrt_message))





    return Response("success")

if __name__ == '__main__':
    app.run(port=5002)
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
