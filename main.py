import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from googletrans import Translator, constants
from pprint import pprint

# twitter tokens
# consumer_key = "KMHqdARHyhMg81fKFSz1NCUKo"
# consumer_secret = "BtSrSMZlwi8fELWgusjbg7bqTqZQAvr5nbGftnoyip97ucmawJ"
# access_token = "2815936960-tlBGLG76LidG7athISfkKA88WF1QQDGpZPsBmFc"
# access_token_secret = "KnPIewl3anX8smJB3rZFF7a1e5ZtqqzfJa72idX0XGNN4"
#
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth,wait_on_rate_limit=True)
# username='elonmusk'
# tweets_list= api.user_timeline(username, count=1)
# tweet= tweets_list[0] # An object of class Status (tweepy.models.Status)
# print(tweet.created_at)
# print(tweet.text)

translator = Translator()

# Aiogram'i yapılandırma
API_TOKEN = '6288578757:AAFMc2YqbDL24-AY1MWpSZF6er6SuTa1LLE'  # Telegram Bot API tokenını buraya girin
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['translate'])
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    translation = translator.translate(text, src="tr")
    trans = f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"
    await message.reply(trans)


@dp.message_handler(commands=['poll'])
async def poll(message: types.Message):
    await message.answer_poll(question='Your answer?',
                              options=['A)', 'B)', 'C'],
                              type='quiz',
                              correct_option_id=1,
                              is_anonymous=False)


async def scheduled_job():
    pass


# /start komutuna yanıt verme
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(
        "Bot aktif! Merhaba demek için /hello komutunu kullanın. \n Çeviri yapmak için /translate komutunu kullanın. \n Kelime testi yapmak için /test komutunu kullanın.")


# /test komutu
@dp.message_handler(Command("test"))
async def test(message: types.Message):
    await message.reply("test kodu başarılı")


# Bot'u çalıştırma
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
