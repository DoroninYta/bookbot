import asyncio

from aiogram import Dispatcher, Bot, Router
from config_data.config import load_config, Config
from handlers import
from keyboards import 

async def main():
    config : Config = load_config()
    bot = Bot(token = config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router
    # menu
    await dp.start_pooling(bot)

asyncio.run(main)
    
