from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '6512132416:AAG9kxa5ZFP6-7ZxX8OsIEvKz8WGcHoUSiM'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start', 'help']))
async def process_start_command(message:Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')






@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text=('''Данный тип апдейтов не поддерживается 
                 'методом send_copy'''))


if __name__ == '__main__':
    dp.run_polling(bot)