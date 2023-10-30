import os
import telebot
import schedule
import requests
import time
from dotenv import load_dotenv
load_dotenv()

chat_ids = [1217268095]

CMC_API_KEY = os.getenv('CMC_API_KEY')
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

def get_cmc_data() -> dict:
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  response = requests.get(url, headers={'X-CMC_PRO_API_KEY': CMC_API_KEY})
  obj = response.json()
  print('------------------', obj)

  btc = 0
  eth = 0
  bnb = 0
  for item in obj['data']:
    price = round(item['quote']['USD']['price'], 1)
    match item['symbol']:
      case 'BTC':
        btc = price
      case 'ETH':
        eth = price
      case 'BNB':
        bnb = price
  return f'Morning sir!\n*Crypto report for today:*\n*BTC* -> {btc}\n*ETH* -> {eth}\n*BNB* -> {bnb}\n'

for id in chat_ids:
  bot.send_message(chat_id=id, text=get_cmc_data(), parse_mode="Markdown")

# def send_test():
#   for id in chat_ids:
#     bot.send_message(chat_id=id,text='Test hihi!!!')

# schedule.every().day.at('00:39').do(send_test)

# print('Running...')

#   schedule.run_pending()
#   time.sleep(1)