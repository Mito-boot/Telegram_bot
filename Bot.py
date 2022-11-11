from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
TOKEN = '5696739138:AAF5mpA3viOglCaN-8sVSF-i6VFNZseBDV8'
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def send_welcome(msg: types.Message):
    await msg.answer(f'Я бот.Приятно познакомиться, {msg.from_user.first_name}')

f = open('text.txt')

markup = types.InlineKeyboardMarkup(row_width=3)
item1 = types.InlineKeyboardButton('AUX', callback_data='aux')
item2 = types.InlineKeyboardButton('Платки', callback_data='platki')
item3 = types.InlineKeyboardButton('Чехол', callback_data='chehol')
markup.add(item1,item2,item3)
@dp.callback_query_handler(func=lambda call:True)
async def callback_inline(call):
    try:
        if call.message:
            if call.data == 'aux':


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Выбери что ты сегодня делала)', reply_markup=markup)
   else:
       await msg.answer('Не понимаю, что это значит.')

# @dp.message_handler(content_types=['text'])
# async def adding_values(msg: types.Message):
#

if __name__ == '__main__':
    executor.start_polling(dp)